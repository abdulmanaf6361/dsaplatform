from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from accounts.models import User
from submissions.models import Submission
from questions.models import Day

@login_required
def leaderboard(request):
    from accounts.models import Batch
    students = User.objects.filter(is_trainer=False, is_superuser=False)
    
    selected_batch = request.GET.get('batch')
    batches = Batch.objects.all()
    
    if not (request.user.is_trainer or request.user.is_superuser):
        selected_batch = request.user.batch_name
        
    if selected_batch:
        students = students.filter(batch_name=selected_batch)

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
        'batches': batches,
        'selected_batch': selected_batch,
    })
