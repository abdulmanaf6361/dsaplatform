# practice/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages

from django.http import JsonResponse
from .models import PracticeDay, PracticeQuestion, PracticeTestCase, PracticeSubmission, PracticeTestResult
from submissions.executor import judge
import json

@login_required
def practice_dashboard(request):
    days = PracticeDay.objects.prefetch_related('questions').all()
    passed_ids = set(
        PracticeSubmission.objects.filter(
            student=request.user, all_passed=True
        ).values_list('question_id', flat=True)
    )
    attempted_ids = set(
        PracticeSubmission.objects.filter(
            student=request.user
        ).values_list('question_id', flat=True)
    )
    return render(request, 'practice/dashboard.html', {
        'days': days,
        'passed_ids': passed_ids,
        'attempted_ids': attempted_ids,
    })

@login_required
def practice_question(request, question_id):
    question = get_object_or_404(PracticeQuestion, id=question_id)
    if not question.day.is_unlocked:
        messages.warning(request, 'This practice day is not unlocked yet.')
        return redirect('practice_dashboard')
    sample_cases = question.test_cases.filter(is_sample=True)
    last_sub = PracticeSubmission.objects.filter(
        student=request.user, question=question
    ).order_by('-submitted_at').first()
    return render(request, 'practice/question.html', {
        'question': question,
        'sample_cases': sample_cases,
        'last_submission': last_sub,
        'last_code_body': last_sub.code if last_sub else '',
        'signature_line': question.function_signature,
        'total_cases': question.test_cases.count(),
    })

@login_required
def practice_run(request, question_id):
    question = get_object_or_404(PracticeQuestion, id=question_id)
    if not question.day.is_unlocked:
        return JsonResponse({'error': 'Day not unlocked'}, status=403)
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    data = json.loads(request.body)
    raw_code = data.get('code', '')
    # ACE editor sends full code including signature — use as-is
    full_code = raw_code.replace('\r\n', '\n').replace('\r', '\n').strip()
    if not full_code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    test_cases = list(question.test_cases.all())
    results = judge(full_code, question.wrapper_code, test_cases)
    passed_count = sum(1 for r in results if r['passed'])

    return JsonResponse({
        'results': [
            {
                'tc_number': i + 1,
                'passed': r['passed'],
                'input': r['test_case'].input_data,
                'actual': r['actual_output'],
                'expected': r['expected_output'],
                'error': r['error'],
                'is_sample': r['test_case'].is_sample,
            }
            for i, r in enumerate(results)
        ],
        'passed_count': passed_count,
        'total_count': len(results),
        'all_passed': passed_count == len(results),
    })

@login_required
def practice_submit(request, question_id):
    question = get_object_or_404(PracticeQuestion, id=question_id)
    if not question.day.is_unlocked:
        messages.warning(request, 'This practice day is not unlocked yet.')
        return redirect('practice_dashboard')
    if request.method != 'POST':
        return redirect('practice_question', question_id=question_id)

    # ACE editor sends full code including signature — use as-is
    full_code = request.POST.get('code', '').replace('\r\n', '\n').replace('\r', '\n').strip()
    if not full_code:
        messages.error(request, 'No code to submit.')
        return redirect('practice_question', question_id=question_id)

    test_cases = list(question.test_cases.all())
    results = judge(full_code, question.wrapper_code, test_cases)

    passed_count = sum(1 for r in results if r['passed'])
    total_count = len(results)
    all_passed = passed_count == total_count

    sub = PracticeSubmission.objects.create(
        student=request.user, question=question,
        code=full_code, all_passed=all_passed,
        total_cases=total_count, passed_cases=passed_count,
    )
    for r in results:
        PracticeTestResult.objects.create(
            submission=sub, test_case=r['test_case'],
            passed=r['passed'], actual_output=r['actual_output'],
            error=r['error'],
        )
    return redirect('practice_result', submission_id=sub.id)

@login_required
def practice_result(request, submission_id):
    sub = get_object_or_404(PracticeSubmission, id=submission_id, student=request.user)
    results = sub.results.select_related('test_case').all()
    return render(request, 'practice/result.html', {'submission': sub, 'results': results})

@login_required
def practice_my_submissions(request, question_id):
    question = get_object_or_404(PracticeQuestion, id=question_id)
    subs = PracticeSubmission.objects.filter(student=request.user, question=question)
    return render(request, 'practice/my_submissions.html', {'question': question, 'submissions': subs})

# ── Trainer views ──────────────────────────────────────────────
@staff_member_required
def trainer_practice_dashboard(request):
    days = PracticeDay.objects.prefetch_related('questions').all()
    from accounts.models import User
    total_students = User.objects.filter(is_staff=False, is_superuser=False).count()
    total_subs = PracticeSubmission.objects.count()
    return render(request, 'practice/trainer_dashboard.html', {
        'days': days,
        'total_students': total_students,
        'total_subs': total_subs,
    })

@staff_member_required
def trainer_toggle_practice_day(request, day_id):
    day = get_object_or_404(PracticeDay, id=day_id)
    if request.method == 'POST':
        day.is_unlocked = not day.is_unlocked
        day.save()
        status = 'unlocked' if day.is_unlocked else 'locked'
        messages.success(request, f'Practice Day {day.day_number} is now {status}.')
    return redirect('trainer_practice_dashboard')

@staff_member_required
def trainer_practice_submissions(request):
    from accounts.models import User
    subs = PracticeSubmission.objects.select_related(
        'student', 'question', 'question__day'
    ).order_by('-submitted_at')

    student_id = request.GET.get('student')
    day_id = request.GET.get('day')
    if student_id:
        subs = subs.filter(student_id=student_id)
    if day_id:
        subs = subs.filter(question__day_id=day_id)

    students = User.objects.filter(is_staff=False, is_superuser=False)
    days = PracticeDay.objects.all()
    return render(request, 'practice/trainer_submissions.html', {
        'submissions': subs[:100],
        'students': students,
        'days': days,
        'selected_student': student_id,
        'selected_day': day_id,
    })

@staff_member_required
def trainer_practice_submission_detail(request, submission_id):
    sub = get_object_or_404(PracticeSubmission, id=submission_id)
    results = sub.results.select_related('test_case').all()
    return render(request, 'practice/trainer_submission_detail.html', {
        'submission': sub, 'results': results,
    })

@staff_member_required
def trainer_practice_progress(request):
    from accounts.models import User
    students = User.objects.filter(is_staff=False, is_superuser=False)
    data = []
    for student in students:
        passed = PracticeSubmission.objects.filter(
            student=student, all_passed=True
        ).values('question').distinct().count()
        attempted = PracticeSubmission.objects.filter(
            student=student
        ).values('question').distinct().count()
        data.append({'student': student, 'passed': passed, 'attempted': attempted})
    data.sort(key=lambda x: x['passed'], reverse=True)
    return render(request, 'practice/trainer_progress.html', {'data': data})