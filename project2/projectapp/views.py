from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login

from django.shortcuts import render,redirect

from projectapp.form import Stud_Form, Admin_Form,user_register,markform

from projectapp.models import Stud_reg,mark

from django.contrib.auth import logout

# Create your views here.

def first(request):
    return render(request,'home.html')


def log(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user is not None and user.is_admin:
                return redirect('adminpage')
            elif user is not None and user.is_student:
                return redirect('studpage')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'mainlogin.html')


def student_sign(request):
    u_form = user_register()
    s_form = Stud_Form()
    if request.method=="POST":
        u_form = user_register(request.POST)
        s_form = Stud_Form(request.POST,request.FILES)
        if u_form.is_valid() and s_form.is_valid():
            user = u_form.save(commit=False)
            user.is_student = True
            user.save()
            student = s_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'student registration successful')
            return redirect('log')

    return render(request, 'studentlogin.html',{'u_form':u_form,'s_form':s_form})


def admin_sign(request):
    u_form = user_register()
    a_form = Admin_Form()
    if request.method=="POST":
        u_form = user_register(request.POST)
        a_form = Admin_Form(request.POST)
        if u_form.is_valid() and a_form.is_valid():
            user = u_form.save(commit=False)
            user.is_admin = True
            user.save()
            admin = a_form.save(commit=False)
            admin.user = user
            admin.save()
            messages.info(request, 'admin registration successful')
            return redirect('log')

    return render(request, 'adminlogin.html',{'u_form':u_form,'a_form':a_form})


@login_required(login_url='log')
def studpage(request):
    return render(request,'studentpage.html')


@login_required(login_url='log')
def adminpage(request):
    return render(request,'adminpage.html')


@login_required(login_url='log')
def studentview(request):
    data=Stud_reg.objects.all()
    return render(request,'studentview.html',{'data':data})


@login_required(login_url='log')
def add_mark(request):
    form = markform()
    if request.method == "POST":
        form = markform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_mark')
    return render(request, 'addmark.html', {'form': form})


@login_required(login_url='log')
def view_mark(request):
    data = mark.objects.all()
    return render(request, 'viewmark.html', {'data': data})



@login_required(login_url='log')
def mark_update(request,id):
    mark1=mark.objects.get(id=id)
    form=markform(instance=mark1)
    if request.method=="POST":
        form=markform(request.POST,instance=mark1)
    if form.is_valid():
        form.save()
        return redirect('view_mark')
    return render(request,'addmark.html',{'form':form})


@login_required(login_url='log')
def mark_delete(request,id):
    mark.objects.get(id=id).delete()
    return redirect('view_mark')



@login_required(login_url='log')
def view_mark_stud(request):
    u = Stud_reg.objects.get(user=request.user)
    data = mark.objects.filter(name=u)
    return render(request, 'viewmark_student.html', {'data': data})


@login_required(login_url='log')
def stud_profile_view(request):
    student = Stud_reg.objects.get(user=request.user)
    return render(request,'studprofileview.html',{'student':student})


@login_required(login_url='log')
def profile_edit(request):
    profile1=Stud_reg.objects.get(user=request.user)
    form=Stud_Form(instance=profile1)
    if request.method=="POST":
        form=Stud_Form(request.POST,request.FILES,instance=profile1)
    if form.is_valid():
        form.save()
        return redirect('stud_profile_view')
    return render(request,'profile_edit.html',{'form':form})




def logout_stud(request):
    logout(request)
    return redirect('first')


def logout_admin(request):
    logout(request)
    return redirect('first')







