from django.contrib import admin
from .models import Course, Discount, Lesson, Lead

# Register your models here.

admin.site.register(Course)
admin.site.register(Discount)
admin.site.register(Lesson)
admin.site.register(Lead)

