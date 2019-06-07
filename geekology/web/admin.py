from django.contrib import admin
from .models import Student,Skill,StudentSkill,Label

# Register your models here.
admin.site.register(Student)
admin.site.register(Skill)
admin.site.register(StudentSkill)
admin.site.register(Label)