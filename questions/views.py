from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Day, Question

@login_required
def dashboard(request):
    days = Day.objects.prefetch_related('questions', 'unlocked_batches').all()
    from submissions.models import Submission
    from django.db import models
    
    unlocked_day_ids = set(
        Day.objects.filter(
            unlocked_batches__name=request.user.batch_name
        ).values_list('id', flat=True)
    )
    
    passed_question_ids = set(
        Submission.objects.filter(
            student=request.user, all_passed=True
        ).values_list('question_id', flat=True)
    )
    return render(request, 'questions/dashboard.html', {
        'days': days,
        'passed_question_ids': passed_question_ids,
        'unlocked_day_ids': unlocked_day_ids,
    })

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if not question.day.unlocked_batches.filter(name=request.user.batch_name).exists():
        messages.warning(request, 'This day is not unlocked yet.')
        return redirect('dashboard')

    sample_cases = question.test_cases.filter(is_sample=True)
    from submissions.models import Submission
    last_submission = Submission.objects.filter(
        student=request.user, question=question
    ).order_by('-submitted_at').first()

    return render(request, 'questions/question_detail.html', {
        'question': question,
        'sample_cases': sample_cases,
        'last_submission': last_submission,
        'last_code_body': last_submission.code if last_submission else '',
        'signature_line': question.function_signature,
        'total_cases': question.test_cases.count(),
    })