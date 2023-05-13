from django.db import models

class Student(models.Model):
    student_name = models.TextField()

    def __str__(self):
        return self.student_name

class Event(models.Model):
    event_name = models.TextField()

    def __str__(self):
        return self.event_name

class Point(models.Model):
    student = models.ForeignKey(
        Student,
        related_name='points',
        on_delete=models.CASCADE
    )
    event = models.ForeignKey(
        Event,
        related_name='points',
        on_delete=models.CASCADE
    )
    point = models.IntegerField()

    class Meta:
        unique_together = ('student', 'event')
