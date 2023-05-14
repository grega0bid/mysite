import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question

# Create your tests here.

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently returns False če je pub_date in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        furure_question = Question(pub_date=time)
        self.assertIs(furure_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        Returns False če je published starejši od enega dneva
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        Returns True če je pub_date mlajši od dneva
        """ 
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def create_question(question_text, days):
        """
        Naredi question_text in ga objavi na dan, ki ga izbereš + ali - dan
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)
    
   