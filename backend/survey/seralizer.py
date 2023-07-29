from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate



''' Model Inputs'''
from .models import Survey
from .models import Questions
from .models import Responses




'''
-> Create Method for user Registration 

-> Meta class for modelserializer

'''

class RegisterSeralizer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password=validated_data['password']
        )
        return user




'''

-> Validate method == Checks username and password
                   == Checks authenciate user status

'''
class LoginSeralizer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError('Incorrect crediential. Please try again')
        else:
            raise serializers.ValidationError('username or password is empty')
        
        return user
    


'''

-> Model to include all the fields 

'''


class SurveySeralizer(serializers.ModelSerializer):

    class Meta:
        model = Survey
        fields = ('id','sruvey_name','description')
    

'''

-> Model to include all the fields
 
'''

class QuestionsSeralizer(serializers.ModelSerializer):
    class Meta:
        model  = Questions
        fields = ('id','question','type')


'''

-> Model to include all the fields

'''

class ResponsesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Responses
        fields = ('id','reponse','user_id')
