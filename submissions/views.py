from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from questions.models import Question
from questions.signatures import SIGNATURES
from .models import Submission, TestResult
from .executor import judge
import json
import logging

logger = logging.getLogger(__name__)

def get_signature_data(question):
    key = (question.day.day_number, question.order)
    return SIGNATURES.get(key, {
        "signature": "def solution():",
        "wrapper": "def _run(input_str):\n    return str(solution())\n"
    })

@login_required
def run_code(request, question_id):
    """AJAX endpoint — runs code and returns results without saving."""
    question = get_object_or_404(Question, id=question_id)
    if not question.day.is_unlocked:
        return JsonResponse({'error': 'Day not unlocked'}, status=403)
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    data = json.loads(request.body)
    raw_code = data.get('code', '')

    logger.warning("RAW CODE REPR: %r", raw_code[:200])

    # Strip ALL carriage returns aggressively
    student_code = raw_code.replace('\r\n', '\n').replace('\r', '\n').strip()
    logger.warning("CLEAN CODE REPR: %r", student_code[:200])

    if not student_code:
        return JsonResponse({'error': 'No code provided'}, status=400)

    sig_data = get_signature_data(question)
    
    # FIX: The function signature is now part of the editor code.
    # We no longer prepend or indent the student code.
    full_student_code = student_code
    
    test_cases = list(question.test_cases.all())
    results = judge(full_student_code, sig_data['wrapper'], test_cases)

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
def submit_code(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if not question.day.is_unlocked:
        messages.warning(request, 'This day is not unlocked yet.')
        return redirect('dashboard')
    if request.method != 'POST':
        return redirect('question_detail', question_id=question_id)

    # Strip ALL carriage returns aggressively
    student_code = request.POST.get('code', '').replace('\r\n', '\n').replace('\r', '\n').strip()
    if not student_code:
        messages.error(request, 'No code to submit.')
        return redirect('question_detail', question_id=question_id)

    sig_data = get_signature_data(question)
    
    # FIX: The function signature is now part of the editor code.
    # We no longer prepend or indent the student code.
    full_student_code = student_code
    
    test_cases = list(question.test_cases.all())
    results = judge(full_student_code, sig_data['wrapper'], test_cases)

    passed_count = sum(1 for r in results if r['passed'])
    total_count = len(results)
    all_passed = passed_count == total_count

    submission = Submission.objects.create(
        student=request.user, question=question,
        code=student_code,  # Save the full code (including signature)
        all_passed=all_passed,
        total_cases=total_count,
        passed_cases=passed_count,
    )
    for r in results:
        TestResult.objects.create(
            submission=submission,
            test_case=r['test_case'],
            passed=r['passed'],
            actual_output=r['actual_output'],
            error=r['error'],
        )
    return redirect('submission_result', submission_id=submission.id)

@login_required
def submission_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id, student=request.user)
    results = submission.results.select_related('test_case').all()
    return render(request, 'submissions/result.html', {
        'submission': submission,
        'results': results,
    })

@login_required
def my_submissions(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    submissions = Submission.objects.filter(
        student=request.user, question=question
    ).order_by('-submitted_at')
    return render(request, 'submissions/my_submissions.html', {
        'question': question,
        'submissions': submissions,
    })