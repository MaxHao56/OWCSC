from django.urls import path

from .views import register_api
from .views import login_api
from .views import user_profile

urlpatterns = [
    path('api/register',register_api, name='Register API'),
    path('api/login',login_api, name="Login API"),
    path('api/user',user_profile, name='user')
]