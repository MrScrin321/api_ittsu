from rest_framework import serializers
from points.models import Point, Student, Event


class EventSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField()

    class Meta:
        model = Event
        fields = ('event_name')    


class PointSerializer(serializers.ModelSerializer):
    student = serializers.CharField()
    event = serializers.CharField()

    class Meta:
        model = Point
        fields = ('student', 'event', 'point')


class StudentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField()
    points = PointSerializer(read_only=True, many=True)

    class Meta:
        model = Student
        fields = ('id', 'student_name', 'points')
