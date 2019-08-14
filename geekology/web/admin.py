from django.contrib import admin
from .models import Student,Skill,StudentSkill,Label


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','studentName','studentNumber','phoneNumber','email']
    search_fields = ['studentName','studentNumber']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id','skillName','categorylabel']
    search_fields = ['skillName']

@admin.register(StudentSkill)
class StudentSkillAdmin(admin.ModelAdmin):
    list_display = ['id','student','skill','level']
    list_filter = ['level']

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id','labelName','persianTrans']
    search_fields = ['labelName']
