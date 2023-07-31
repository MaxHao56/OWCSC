from django.urls import path


''' View(api) Imports'''

from .views import user_profile



from . import html
from .html import survey_view
from .html import question_view
from .html import questions_view

from . import views

urlpatterns = [

    path('api/user',user_profile, name='user'),
    path('api/logout',views.process_logout,name='Logout'),



    path('register',html.register_view,name='register_view'),
    path('login',html.login_view, name='login_view'),
    path('',html.home_view,name='home_view'),





    path('survey',survey_view),
    path('question',question_view),
    path('questions',questions_view),


    path('form/',views.process_register_form, name='process_register_form'),
    path('loginform',views.process_login_form,name='process_login_form'),
    
    
    
]