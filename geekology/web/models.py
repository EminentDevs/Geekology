from django.db import models

# True/False as 1/0
class CustomBooleanField(models.BooleanField):
    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return int(value) # return 0/1

# Create your models here.

class Student(models.Model):
    studentName = models.CharField(max_length=100)
    male = CustomBooleanField(null=True)
    birthdayDate = models.CharField(max_length=4,null=True)
    studentNumber = models.CharField(max_length=15)
    enterYear = models.CharField(max_length=4,null=True)
    gender = models.CharField(max_length=1,null=True)
    email = models.EmailField(max_length=50,null=True)
    pWebUrl = models.URLField(max_length=50,null=True)
    phoneNumber = models.CharField(max_length=11)
    telegram = models.CharField(max_length=20,null=True)
    instagram = models.CharField(max_length=20,null=True)

    def __str__(self):
        return '{} - {}'.format(self.studentName,self.studentNumber)

class Skill(models.Model):
    skillName = models.CharField(max_length=40)
    def __str__(self):
        return '{}'.format(self.skillName)

class StudentSkill(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
    level = models.CharField(max_length=1,default='0')
    def __str__(self):
        return '{} - {} - {}'.format(self.student,self.skill,self.level)
