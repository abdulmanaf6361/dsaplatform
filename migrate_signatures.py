"""
One-time script: populates function_signature and wrapper_code
on all existing Question rows from signatures.py.
Run: python migrate_signatures.py
"""
import os, django, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dsaplatform.settings')
sys.path.insert(0, '.')
django.setup()

from questions.models import Question
from questions.signatures import SIGNATURES

updated = 0
missing = []

for question in Question.objects.select_related('day').all():
    key = (question.day.day_number, question.order)
    sig_data = SIGNATURES.get(key)
    if sig_data:
        question.function_signature = sig_data['signature']
        question.wrapper_code = sig_data['wrapper']
        question.save(update_fields=['function_signature', 'wrapper_code'])
        updated += 1
    else:
        missing.append(f"Day {question.day.day_number} Q{question.order}: {question.title}")

print(f"Updated: {updated} questions")
if missing:
    print(f"Missing signatures for {len(missing)} questions:")
    for m in missing:
        print(f"  - {m}")
else:
    print("All questions have signatures!")