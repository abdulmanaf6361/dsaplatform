from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from accounts.models import User
from submissions.models import Submission
from questions.models import Day

@login_required
def leaderboard(request):
    # Get all non-trainer students
    students = User.objects.filter(is_trainer=False, is_superuser=False)

    board = []
    for student in students:
        passed_count = Submission.objects.filter(
            student=student, all_passed=True
        ).values('question').distinct().count()
        board.append({
            'student': student,
            'passed_count': passed_count,
        })

    board.sort(key=lambda x: x['passed_count'], reverse=True)

    # Add rank
    for i, entry in enumerate(board):
        entry['rank'] = i + 1

    total_questions = 57
    return render(request, 'leaderboard/leaderboard.html', {
        'board': board,
        'total_questions': total_questions,
    })
