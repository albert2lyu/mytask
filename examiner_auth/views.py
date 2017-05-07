from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from models import UserProfile, StudyTeam, Grade

def user_register(request) : 
    studyteams = StudyTeam.objects.all()
    grades = Grade.objects.all()
    
    user_, user_created_ = User.objects.get_or_create(username = request.POST.get('username', False))
    if user_created_ : 
        # already exists
        return redirect('/accounts/login/')
    user_.password = request.POST.get('password', False)
    studyTeam_, team_created_ = StudyTeam.objects.get_or_create(studyTeam = request.POST.get('studyTeam', False))
    grade_, grade_created_ = Grade.objects.get_or_create(grade = request.POST.get('grade', False))
 
    profileUser = UserProfile.objects.create(user = user_, \
        nameZh = request.POST.get('nameZh', False), \
        examinationCode = request.POST.get('examinationCode', False), \
        studyTeam = studyTeam_, \
        grade = grade_)
    user_.save()
    profileUser.save()
    return render(request, 'register.html', \
        {'studyteams' : studyteams, \
        'grades' : grades})

def user_logout(request) : 
    logout(request)
    return redirect('/')    

def user_login(request) : 
    user = authenticate(username = request.POST.get('username', ''), \
        password = request.POST.get('password', ''))
    if user is not None : 
        if user.is_active : 
            login(request, user)
            return render(request, 'home.html')
        else : 
            pass
            # this account is disabled
    return render(request, 'login.html')
    # else : 
    #     return redirect('/accounts/register/')