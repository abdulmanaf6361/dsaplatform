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
    list_display = ['day_number', 'title', 'is_unlocked']
    list_editable = ['is_unlocked']
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'difficulty', 'day']
    list_filter = ['day', 'difficulty']
    inlines = [TestCaseInline]

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_sample', 'order']
