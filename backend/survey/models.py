from django.db import models

'''
-> Model for Survey
'''
class Survey(models.Model):
    sruvey_name = models.CharField(max_length=50)
    description = models.TextField()

'''
-> Model for Questions
'''
class Questions(models.Model):
    question = models.TextField()
    type = models.CharField()

'''
-> Model for Responses
'''
class Responses(models.Model):
    response = models.JSONField(default=dict)
    user_id = models.TextField(default='')


