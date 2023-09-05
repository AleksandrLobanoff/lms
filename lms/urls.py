from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentsListAPIView

from lms.apps import LmsConfig

app_name = LmsConfig.name


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='courses')

urlpatterns = [
path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

path('payments', PaymentsListAPIView.as_view(), name='payments-list'),

] + router.urls
