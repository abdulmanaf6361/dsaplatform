from django.db import models

class Day(models.Model):
    day_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    topics = models.TextField(help_text='Topics covered this day')
    unlocked_batches = models.ManyToManyField('accounts.Batch', blank=True)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f'Day {self.day_number}: {self.title}'

class Question(models.Model):
    DIFFICULTY_CHOICES = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='questions')
    order = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField()
    input_format = models.TextField(blank=True)
    output_format = models.TextField(blank=True)
    constraints = models.TextField(blank=True)
    sample_input = models.TextField(blank=True)
    sample_output = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='easy')
    # Signature and wrapper stored in DB — editable from admin
    function_signature = models.CharField(max_length=200, blank=True)
    wrapper_code = models.TextField(blank=True)

    class Meta:
        ordering = ['day', 'order']

    def __str__(self):
        return f'Day {self.day.day_number} Q{self.order}: {self.title}'

class TestCase(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='test_cases')
    input_data = models.TextField()
    expected_output = models.TextField()
    is_sample = models.BooleanField(default=False)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'TC{self.order} for {self.question.title}'