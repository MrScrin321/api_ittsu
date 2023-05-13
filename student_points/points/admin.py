from django.contrib import admin
from .models import Student, Event, Point

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name')
    search_fields = ('student_name',)
    list_filter = ('student_name',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name')
    search_fields = ('event_name',)
    list_filter = ('event_name',)

class PointAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'event', 'point')
    search_fields = ('student',)
    list_filter = ('student', 'event')

admin.site.register(Student, StudentAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Point, PointAdmin)
