from rest_framework import serializers
from stories.models import Story, Reader
from django.contrib.auth import get_user_model

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'title', 'author', 'link']

User = get_user_model()

def create_reader(user):
    Reader.objects.create(user=user)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # Create associated Reader object when a new user signs up
        create_reader(user)

        return user
