from django.contrib import admin
from .models import PracticeDay, PracticeQuestion, PracticeTestCase, PracticeSubmission, PracticeTestResult

class PracticeTestCaseInline(admin.TabularInline):
    model = PracticeTestCase
    extra = 2

class PracticeQuestionInline(admin.TabularInline):
    model = PracticeQuestion
    extra = 0
    show_change_link = True

@admin.register(PracticeDay)
class PracticeDayAdmin(admin.ModelAdmin):
    list_display = ['day_number', 'title', 'get_unlocked_batches']
    inlines = [PracticeQuestionInline]
    filter_horizontal = ('unlocked_batches',)

    def get_unlocked_batches(self, obj):
        return ", ".join([b.name for b in obj.unlocked_batches.all()])
    get_unlocked_batches.short_description = 'Unlocked Batches'

@admin.register(PracticeQuestion)
class PracticeQuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'difficulty']
    list_filter = ['day', 'difficulty']
    inlines = [PracticeTestCaseInline]

class PracticeTestResultInline(admin.TabularInline):
    model = PracticeTestResult
    readonly_fields = ['test_case', 'passed', 'actual_output', 'error']
    extra = 0

@admin.register(PracticeSubmission)
class PracticeSubmissionAdmin(admin.ModelAdmin):
    list_display = ['student', 'question', 'all_passed', 'passed_cases', 'total_cases', 'submitted_at']
    inlines = [PracticeTestResultInline]
