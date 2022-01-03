from rest_framework.serializers import ModelSerializer
from .models import User, Course, Lesson, Tag

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': { 'write_only': True },
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'description', 'created_date', 'category']
        extra_kwargs = {
            'image': { 'required': False },
            'description': { 'required': False },
        }

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    tag = TagSerializer(many=True, required=False)
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'content', 'created_date', 'course', 'tag']
        extra_kwargs = {
            'image': { 'required': False },
            'content': { 'required': False },
        }
