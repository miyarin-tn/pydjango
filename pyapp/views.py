from django.http.response import HttpResponse
from django.views import View
from rest_framework import generics, viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import User, Course, Lesson
from .serializers import UserSerializer, CourseSerializer, LessonSerializer

# Create your views here.
class UserViewSet(viewsets.ViewSet, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser,]

    def get_permissions(self):
        if self.action == 'retrieve':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    @action(methods=['post'], detail=True, url_path='hide-lesson', url_name='hide-lesson')
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)


def welcome(request):
    return HttpResponse('Hello')

def welcome_detail(request, year):
    return HttpResponse('Hello ' + str(year))

def welcome_other(request, year):
    return HttpResponse('Hello ' + str(year))


class TestView(View):
    def get(self, request):
        return HttpResponse('Get view test')

    def post(self, request):
        pass
