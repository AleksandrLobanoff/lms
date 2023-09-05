from rest_framework import serializers

from lms.models import Course, Lesson, Payments


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    lessons_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        lessons_count = obj.lessons.all()
        if lessons_count:
            return len(lessons_count)
        return 0

    class Meta:
        model = Course
        fields = '__all__'


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
