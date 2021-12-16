from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
from Student_Registration.models import teacher
@csrf_protect
def Home(request):
    responses=render(request,'Home.html')
    return responses
def signup(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['useremail']
        password=request.POST['password1']
        passwordconfirm=request.POST['password2']
        gender=request.POST['gender']
        users=User.objects.create_user(username,email,password)
        users.first_name=firstname
        users.last_name=lastname
        users.confirm_password=passwordconfirm
        users.user_gender=gender
        users.save()
        messages.success(request,"Your Account has been successfull created")
        return redirect('http://localhost:8000/Student_Registration/login')
    return render(request,'register.html')
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request,'Home.html',{"fname":fname})
        else:
            messages.error(request,"Username and Password may Incorrect")
            return redirect('http://localhost:8000/Student_Registration/home')
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('http://localhost:8000/Student_Registration/home')
def teacher_joining(request):
    if request.method=='POST':
        teacherdata=request.POST
        teachers=teacher()
        teachers.firstname=teacherdata['firstname']
        teachers.lastname=teacherdata['lastname']
        teachers.teachername=teacherdata['teachername']
        teachers.teacheremail=teacherdata['emailid']
        teachers.mobilenumber=teacherdata['mobilenumber']
        teachers.phonenumber=teacherdata['phonenumber']
        teachers.gender=teacherdata['gender']
        teachers.dob_days=teacherdata['days']
        teachers.dob_months=teacherdata['months']
        teachers.dob_years=teacherdata['years']
        teachers.address=teacherdata['address']
        teachers.city=teacherdata['city']
        teachers.pincode=teacherdata['pincode']
        teachers.state=teacherdata['state']
        teachers.country=teacherdata['country']
        teachers.qualification=teacherdata['quali']
        teachers.positionapply=teacherdata['apply']
        teachers.save()
        teacherlist="http://localhost:8000/Student_Registration/teacher-list"
        return HttpResponseRedirect(teacherlist)
    return render(request,'joiningteacher.html')
def teacher_list(request):
    return render(request,'teacherlist.html')
    