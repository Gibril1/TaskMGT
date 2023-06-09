from rest_framework import serializers
from .models import User, WorkersProfile, HODProfile
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkersProfile
        fields = '__all__'




class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model = HODProfile
        fields = '__all__'



class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'Password fields didnt match'})

        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user