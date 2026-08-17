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
    days = PracticeDay.objects.prefetch_related('questions', 'unlocked_batches').all()
    
    unlocked_day_ids = set(
        PracticeDay.objects.filter(
            unlocked_batches__name=request.user.batch_name
        ).values_list('id', flat=True)
    )

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
        'unlocked_day_ids': unlocked_day_ids,
    })

@login_required
def practice_question(request, question_id):
    question = get_object_or_404(PracticeQuestion, id=question_id)
    if not question.day.unlocked_batches.filter(name=request.user.batch_name).exists():
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
    if not question.day.unlocked_batches.filter(name=request.user.batch_name).exists():
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
    if not question.day.unlocked_batches.filter(name=request.user.batch_name).exists():
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
    days = PracticeDay.objects.prefetch_related('questions', 'unlocked_batches').all()
    from accounts.models import User, Batch
    total_students = User.objects.filter(is_staff=False, is_superuser=False).count()
    total_subs = PracticeSubmission.objects.count()
    batches = Batch.objects.all()
    return render(request, 'practice/trainer_dashboard.html', {
        'days': days,
        'total_students': total_students,
        'total_subs': total_subs,
        'batches': batches,
    })

@staff_member_required
def trainer_toggle_practice_day(request, day_id, batch_id):
    day = get_object_or_404(PracticeDay, id=day_id)
    from accounts.models import Batch
    batch = get_object_or_404(Batch, id=batch_id)
    if request.method == 'POST':
        if batch in day.unlocked_batches.all():
            day.unlocked_batches.remove(batch)
            status = 'locked'
        else:
            day.unlocked_batches.add(batch)
            status = 'unlocked'
        messages.success(request, f'Practice Day {day.day_number} is now {status} for {batch.name}.')
    return redirect('trainer_practice_dashboard')

@staff_member_required
def trainer_practice_submissions(request):
    from accounts.models import User, Batch
    subs = PracticeSubmission.objects.select_related(
        'student', 'question', 'question__day'
    ).order_by('-submitted_at')

    student_id = request.GET.get('student')
    day_id = request.GET.get('day')
    batch_name = request.GET.get('batch')
    
    if student_id:
        subs = subs.filter(student_id=student_id)
    if day_id:
        subs = subs.filter(question__day_id=day_id)
    if batch_name:
        subs = subs.filter(student__batch_name=batch_name)

    students = User.objects.filter(is_staff=False, is_superuser=False)
    days = PracticeDay.objects.all()
    batches = Batch.objects.all()
    return render(request, 'practice/trainer_submissions.html', {
        'submissions': subs[:100],
        'students': students,
        'days': days,
        'batches': batches,
        'selected_student': student_id,
        'selected_day': day_id,
        'selected_batch': batch_name,
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
    from accounts.models import User, Batch
    batch_name = request.GET.get('batch')
    students = User.objects.filter(is_staff=False, is_superuser=False)
    if batch_name:
        students = students.filter(batch_name=batch_name)
        
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
    
    batches = Batch.objects.all()
    return render(request, 'practice/trainer_progress.html', {
        'data': data,
        'batches': batches,
        'selected_batch': batch_name
    })