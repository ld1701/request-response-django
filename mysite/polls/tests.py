from django.test import TestCase
from .models import Question
import datetime
from django.utils import timezone

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_date)
        self.assertIs(future_question.was_published_recently(), False)

