from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Skill,StudentSkill,Label

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        if request.POST['name'] != '' and request.POST['stdno'] != '' and request.POST['phonenumber'] != '':
            sStdno = request.POST['stdno']
            if Student.objects.filter(studentNumber=sStdno).exists():
                return render(request,'web/index.html')
            else:
                sName = request.POST['name']
                sSexuality = request.POST['sexuality']
                sbirthyear = request.POST['birthyear']
                sEnterYear = request.POST['enteryear']
                sGender = request.POST['gender']
                sEmail = request.POST['email']
                sSiteUrl = request.POST['siteurl']
                sPhoneNumber = request.POST['phonenumber']
                sTelegramId = request.POST['telegram']
                sInstagramId = request.POST['instagram']
                student = Student(studentName = sName,
                                  male = sSexuality,
                                  birthdayDate = sbirthyear,
                                  enterYear = sEnterYear,
                                  gender = sGender,
                                  email = sEmail,
                                  pWebUrl = sSiteUrl,
                                  phoneNumber=sPhoneNumber,
                                  telegram = sTelegramId,
                                  instagram = sInstagramId,
                                  studentNumber = sStdno)
                student.save()
                for item in Skill.objects.all():
                    studentSkill = StudentSkill(student=student,skill=item,level=request.POST.get(item.skillName,'0'))
                    studentSkill.save()
                skill = Skill.objects.all()
                skillLabel = Label.objects.all()
                context = {
                    'skill' : skill,
                    'skillLabel' : skillLabel
                }
                return render(request,'web/index.html',context=context)
        else:
            skill = Skill.objects.all()
            skillLabel = Label.objects.all()
            context = {
                'skill' : skill,
                'skillLabel' : skillLabel
            }
            return render(request,'web/index.html',context=context)
    else:
        skill = Skill.objects.all()
        skillLabel = Label.objects.all()
        context = {
            'skill' : skill,
            'skillLabel' : skillLabel
        }
        return render(request,'web/index.html',context=context)