from django.shortcuts import render

from .seralizer import RegisterSeralizer
from .seralizer import LoginSeralizer


from rest_framework.decorators import api_view  # API VIEW FOR DATABASE INTERACTIONS
from rest_framework.response import Response # Rest framwork for response and HTTP status
from rest_framework import status  # Rest Framwork that really took status to diverse options

from django.contrib.auth import login 
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session

@api_view(['POST'])
def register_api(request):

    seralizer = RegisterSeralizer(data=request.data)
    
    if seralizer.is_valid():
        seralizer.save()
        return Response({'message':'Register Sucessfully'}, status=status.HTTP_201_CREATED)
    
    return Response({'message':'seralizer has errors'}, status=status.HTTP_406_NOT_ACCEPTABLE)



# ISSUE === MUTIPLE KEYS AND REPETITIVE SESSION KEY GENERATION #

'''
@login()

@authenticate()

@seralization

-> user object from validate method from seralizer
-> Returns session key and infomation of the user
'''
@api_view(['POST'])
def login_api(request):

    seralizer = LoginSeralizer(data=request.data)      

    
          
    session = SessionStore()
    if seralizer.is_valid():
        user = seralizer.validate(request.data)


        if user is not None:
            login(request,user)
            
            
            session['user_id'] = user.id
            session['user_username'] = user.username
            session.create()
       

            return Response({'Message':'Login successful','session_key':session.session_key},status=status.HTTP_200_OK)  
        else:
            return Response({'Message':"User is None"},status=status.HTTP_404_NOT_FOUND) 
    else:
        return Response({'Message':'It is not valid'},status=status.HTTP_400_BAD_REQUEST)
    





@api_view(['POST'])
def user_profile(request):
    session_key = request.data.get('session_key')

    try:
        session = Session.objects.get(session_key=session_key)
    except Session.DoesNotExist:
        return Response({'Message': 'Invalid session key'}, status=status.HTTP_404_NOT_FOUND)

    session_data = session.get_decoded()
    username = session_data.get('user_username')

    return Response({'username': username})