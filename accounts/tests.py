from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.test import TestCase


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
