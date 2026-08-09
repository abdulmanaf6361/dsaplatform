from django.db import models
from accounts.models import User

class PracticeDay(models.Model):
    day_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    topics = models.TextField()
    is_unlocked = models.BooleanField(default=False)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f'Practice Day {self.day_number}: {self.title}'

class PracticeQuestion(models.Model):
    DIFFICULTY_CHOICES = [('easy', 'Easy'), ('medium', 'Medium')]
    day = models.ForeignKey(PracticeDay, on_delete=models.CASCADE, related_name='questions')
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    input_format = models.TextField(blank=True)
    output_format = models.TextField(blank=True)
    constraints = models.TextField(blank=True)
    sample_input = models.TextField(blank=True)
    sample_output = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    function_signature = models.CharField(max_length=200)
    wrapper_code = models.TextField()

    class Meta:
        ordering = ['day', 'order']

    def __str__(self):
        return f'P-Day {self.day.day_number} Q{self.order}: {self.title}'

class PracticeTestCase(models.Model):
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='test_cases')
    input_data = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

class PracticeSubmission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='practice_submissions')
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    all_passed = models.BooleanField(default=False)
    total_cases = models.IntegerField(default=0)
    passed_cases = models.IntegerField(default=0)

    class Meta:
        ordering = ['-submitted_at']

class PracticeTestResult(models.Model):
    submission = models.ForeignKey(PracticeSubmission, on_delete=models.CASCADE, related_name='results')
    test_case = models.ForeignKey(PracticeTestCase, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    actual_output = models.TextField(blank=True)
    error = models.TextField(blank=True)
