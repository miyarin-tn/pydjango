from django.urls import path, re_path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('welcome/<int:year>/', views.welcome_detail, name="welcome_detail"),
    re_path(r'welcome_other/(?P<year>[0-9]{4})/$', views.welcome_other, name="welcome_other"),
    path('test/', views.TestView.as_view(), name="test"),
    path('', include(router.urls)),
]
