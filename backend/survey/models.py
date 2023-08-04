from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser





class Survey(models.Model):
    """Survey may have plenty of questions,
    to get access for questions related to survey use 'survey.questions' """
    survey_name = models.CharField(max_length=50, default='', unique=True)
    description = models.TextField(default='empty')

    def __str__(self):
        return self.survey_name

    class Meta:
        verbose_name = 'survey'
        verbose_name_plural = 'surveys'


class Questions(models.Model):
    """ """

    name = models.CharField(max_length=60, default='')
    question = models.TextField(default='empty')

    question_type = models.ForeignKey(
        to=Survey,
        to_field='survey_name',
        on_delete=models.CASCADE,
        related_name='questions',
        default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


'''
-> Model for Responses
'''


class Responses(models.Model):
    class Status(models.TextChoices):
        POSITIVE = 'POS', 'POSITIVE'
        NEGATIVE = 'NEG', 'NEGATIVE'
    response = models.CharField(
        max_length=3,
        choices=Status.choices,
        default=Status.NEGATIVE)
    user = models.ForeignKey(
        to=User,

        on_delete=models.CASCADE,
        related_name='responses',
        default='')
    question = models.ForeignKey(
        to=Questions,
        on_delete=models.CASCADE,
        related_name='responses',
        default='',
        )
    survey_type = models.ForeignKey(to=Survey, to_field='survey_name', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'question')

