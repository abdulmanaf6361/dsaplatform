from django import forms
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.test import TestCase

from .models import Batch
from .forms import StudentRegisterForm


class LogoutTemplateTests(TestCase):
    def test_logout_button_uses_post_form(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username="demo",
            email="demo@example.com",
            password="StrongPass123!",
        )

        html = render_to_string(
            "base.html",
            {"user": user, "messages": []},
        )

        self.assertIn('method="post"', html)
        self.assertIn('action="/accounts/logout/"', html)
        self.assertNotIn('href="/accounts/logout/"', html)


class BatchRegistrationTests(TestCase):
    def test_student_register_form_uses_batch_dropdown(self):
        batch = Batch.objects.create(name="DSA Batch July 2026")

        form = StudentRegisterForm()

        self.assertIsInstance(form.fields['batch_name'], forms.ModelChoiceField)
        self.assertIn(batch, form.fields['batch_name'].queryset)
