from django.contrib import admin
from .models import Day, Question, TestCase

class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    show_change_link = True

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['day_number', 'title', 'get_unlocked_batches']
    inlines = [QuestionInline]
    filter_horizontal = ('unlocked_batches',)

    def get_unlocked_batches(self, obj):
        return ", ".join([b.name for b in obj.unlocked_batches.all()])
    get_unlocked_batches.short_description = 'Unlocked Batches'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'difficulty', 'day']
    list_filter = ['day', 'difficulty']
    inlines = [TestCaseInline]

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_sample', 'order']
