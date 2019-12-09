from django.contrib import admin
from .models import Student, TextAnswer, Question

# Register your models here.
admin.site.register(Student)
admin.site.register(Question)
admin.site.register(TextAnswer)