from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    fullname = serializers.CharField(write_only=True, required=False)
    id = serializers.CharField(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'fullname', 'username', 'email', 'password', ]


    def create(self, validated_data):
        fullname = validated_data.pop('fullname', '')
        password = validated_data.pop('password')

        name_parts = fullname.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''

        user = User(**validated_data)
        user.email = validated_data['username']
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'username' in validated_data and instance.email != validated_data['username']:
            instance.email = validated_data['username']
            instance.username = validated_data['username']
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance
    


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        data['user_id'] = user.id
        data['user_fullname'] = f'{user.first_name} {user.last_name}'
        data['user_email'] = user.email
        data['user_password'] = user.password
        return data
