from django.urls import path


''' View(api) Imports'''
from .views import register_api
from .views import login_api
from .views import user_profile
from .views import getSurvey
from .views import getQuestions
from .views import getResponse

from .html import home_view
from .html import survey_view
from .html import question_view
from .html import questions_view

from . import views

urlpatterns = [
    path('api/register',register_api, name='Register API'),
    path('api/login',login_api, name="Login API"),
    path('api/user',user_profile, name='user'),
    path('get_api/survey', getSurvey,name='Get Surveys'),
    path('get_api/question',getQuestions, name='Get Questions'),
    path('get_api/response',getResponse,name='Get Responses'),


    path('',home_view,name='home_view'),
    path('survey',survey_view),
    path('question',question_view),
    path('questions',questions_view),



    path('form/',views.process_register_form, name='process_register_form')
]