from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


# Seralizer of Registerartion and table Creation

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
    

