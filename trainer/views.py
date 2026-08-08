from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from questions.models import Day, Question
from submissions.models import Submission
from accounts.models import User

@staff_member_required
def trainer_dashboard(request):
    days = Day.objects.prefetch_related('questions').all()
    total_students = User.objects.filter(is_trainer=False, is_superuser=False).count()
    total_submissions = Submission.objects.count()
    return render(request, 'trainer/dashboard.html', {
        'days': days,
        'total_students': total_students,
        'total_submissions': total_submissions,
    })

@staff_member_required
def toggle_day(request, day_id):
    day = get_object_or_404(Day, id=day_id)
    if request.method == 'POST':
        day.is_unlocked = not day.is_unlocked
        day.save()
        status = 'unlocked' if day.is_unlocked else 'locked'
        messages.success(request, f'Day {day.day_number} is now {status}.')
    return redirect('trainer_dashboard')

@staff_member_required
def view_submissions(request):
    submissions = Submission.objects.select_related(
        'student', 'question', 'question__day'
    ).order_by('-submitted_at')

    # Filters
    student_id = request.GET.get('student')
    day_id = request.GET.get('day')
    if student_id:
        submissions = submissions.filter(student_id=student_id)
    if day_id:
        submissions = submissions.filter(question__day_id=day_id)

    students = User.objects.filter(is_trainer=False, is_superuser=False)
    days = Day.objects.all()
    return render(request, 'trainer/submissions.html', {
        'submissions': submissions[:100],
        'students': students,
        'days': days,
        'selected_student': student_id,
        'selected_day': day_id,
    })

@staff_member_required
def view_submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    results = submission.results.select_related('test_case').all()
    return render(request, 'trainer/submission_detail.html', {
        'submission': submission,
        'results': results,
    })

@staff_member_required
def student_progress(request):
    students = User.objects.filter(is_trainer=False, is_superuser=False)
    data = []
    for student in students:
        passed = Submission.objects.filter(
            student=student, all_passed=True
        ).values('question').distinct().count()
        data.append({'student': student, 'passed': passed})
    data.sort(key=lambda x: x['passed'], reverse=True)
    return render(request, 'trainer/student_progress.html', {'data': data})
