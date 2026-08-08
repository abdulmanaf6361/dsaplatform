from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Day, Question
from questions.signatures import SIGNATURES

@login_required
def dashboard(request):
    days = Day.objects.prefetch_related('questions').all()
    from submissions.models import Submission
    passed_question_ids = set(
        Submission.objects.filter(
            student=request.user, all_passed=True
        ).values_list('question_id', flat=True)
    )
    return render(request, 'questions/dashboard.html', {
        'days': days,
        'passed_question_ids': passed_question_ids,
    })

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if not question.day.is_unlocked:
        messages.warning(request, 'This day is not unlocked yet.')
        return redirect('dashboard')

    key = (question.day.day_number, question.order)
    sig_data = SIGNATURES.get(key, {"signature": "def solution():", "wrapper": ""})
    signature_line = sig_data['signature']

    sample_cases = question.test_cases.filter(is_sample=True)
    from submissions.models import Submission
    last_submission = Submission.objects.filter(
        student=request.user, question=question
    ).order_by('-submitted_at').first()

    # Pass last submitted body (without signature line)
    last_code_body = ""
    if last_submission:
        body_lines = last_submission.code.split('\n')
        last_code_body = '\n'.join(body_lines)

    return render(request, 'questions/question_detail.html', {
        'question': question,
        'sample_cases': sample_cases,
        'last_submission': last_submission,
        'last_code_body': last_code_body,
        'signature_line': signature_line,
        'total_cases': question.test_cases.count(),
    })
