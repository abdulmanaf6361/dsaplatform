from django.db import models
from accounts.models import User
from questions.models import Question, TestCase

class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    all_passed = models.BooleanField(default=False)
    total_cases = models.IntegerField(default=0)
    passed_cases = models.IntegerField(default=0)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.student.username} - {self.question.title} - {self.submitted_at}'

class TestResult(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='results')
    test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    actual_output = models.TextField(blank=True)
    error = models.TextField(blank=True)

    def __str__(self):
        status = 'PASS' if self.passed else 'FAIL'
        return f'{status} - TC{self.test_case.order}'
