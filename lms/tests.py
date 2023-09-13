from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from lms.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):
    def create_user(self):
        """Создание пользователя"""
        self.user = User.objects.create(
            email='admin@admin.com',
            is_staff=True,
            is_active=True,
        )
        self.user.set_password('admin')
        self.user.save()

    def setUp(self) -> None:
        """Подготовка данных"""
        self.create_user()

        self.course = Course.objects.create(
            title='course test',
            description='list test description',
            owner=self.user
        )

        self.lesson = Lesson.objects.create(
            title='list test',
            description='list test description',
            owner=self.user
        )

    def test_list_lesson(self):
        """Тестирование вывода списка уроков"""

        response = self.client.get(
            reverse('lms:lessons-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 2, 'course': None, 'title': 'list test', 'description': 'list test description', 'preview': None,
                 'video_link': None, 'owner': 2}]}
        )

    def test_create_lesson(self):
        """Тестирование создания уроков"""
        self.client.force_authenticate(self.user)

        data = {
            'title': 'test',
            'description': 'test description',
            'course': self.course.title,
            'owner': self.user
        }

        response = self.client.post(
            reverse('lms:lesson-create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            Lesson.objects.count(),
            2
        )

    def test_update_lesson(self):
        """Тестирование обновления"""
        self.client.force_authenticate(self.user)
        data = {
            'name': 'test lesson updated',
        }

        response = self.client.patch(
            reverse("courses:lesson-update", kwargs={'pk': self.lesson.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        # Check updated name
        self.assertEqual(
            Lesson.objects.get(pk=1).name,
            'test lesson updated'
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        self.client.force_authenticate(self.user)
        response = self.client.delete(
            reverse("courses:lesson-delete", kwargs={'pk': self.lesson.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lesson.objects.exists()
        )
