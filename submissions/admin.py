from django.contrib import admin
from .models import Submission, TestResult

class TestResultInline(admin.TabularInline):
    model = TestResult
    readonly_fields = ['test_case', 'passed', 'actual_output', 'error']
    extra = 0

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'question', 'all_passed', 'passed_cases', 'total_cases', 'submitted_at']
    list_filter = ['all_passed', 'question__day']
    inlines = [TestResultInline]
