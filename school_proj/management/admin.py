from django.contrib import admin

from .models import (
    Teacher,
    School,
    Class,
    Student,
)

admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Class)
admin.site.register(Student)
