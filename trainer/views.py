from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from questions.models import Day, Question
from submissions.models import Submission
from accounts.models import User, Batch

@staff_member_required
def trainer_dashboard(request):
    days = Day.objects.prefetch_related('questions', 'unlocked_batches').all()
    total_students = User.objects.filter(is_trainer=False, is_superuser=False).count()
    total_submissions = Submission.objects.count()
    batches = Batch.objects.all()
    return render(request, 'trainer/dashboard.html', {
        'days': days,
        'total_students': total_students,
        'total_submissions': total_submissions,
        'batches': batches,
    })

@staff_member_required
def toggle_day(request, day_id, batch_id):
    day = get_object_or_404(Day, id=day_id)
    batch = get_object_or_404(Batch, id=batch_id)
    if request.method == 'POST':
        if batch in day.unlocked_batches.all():
            day.unlocked_batches.remove(batch)
            status = 'locked'
        else:
            day.unlocked_batches.add(batch)
            status = 'unlocked'
        messages.success(request, f'Day {day.day_number} is now {status} for {batch.name}.')
    return redirect('trainer_dashboard')

@staff_member_required
def view_submissions(request):
    submissions = Submission.objects.select_related(
        'student', 'question', 'question__day'
    ).order_by('-submitted_at')

    # Filters
    student_id = request.GET.get('student')
    day_id = request.GET.get('day')
    batch_name = request.GET.get('batch')
    
    if student_id:
        submissions = submissions.filter(student_id=student_id)
    if day_id:
        submissions = submissions.filter(question__day_id=day_id)
    if batch_name:
        submissions = submissions.filter(student__batch_name=batch_name)

    students = User.objects.filter(is_trainer=False, is_superuser=False)
    days = Day.objects.all()
    batches = Batch.objects.all()
    return render(request, 'trainer/submissions.html', {
        'submissions': submissions[:100],
        'students': students,
        'days': days,
        'batches': batches,
        'selected_student': student_id,
        'selected_day': day_id,
        'selected_batch': batch_name,
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
    batch_name = request.GET.get('batch')
    students = User.objects.filter(is_trainer=False, is_superuser=False)
    if batch_name:
        students = students.filter(batch_name=batch_name)
        
    data = []
    for student in students:
        passed = Submission.objects.filter(
            student=student, all_passed=True
        ).values('question').distinct().count()
        data.append({'student': student, 'passed': passed})
    data.sort(key=lambda x: x['passed'], reverse=True)
    
    batches = Batch.objects.all()
    return render(request, 'trainer/student_progress.html', {
        'data': data,
        'batches': batches,
        'selected_batch': batch_name
    })
