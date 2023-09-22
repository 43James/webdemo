from imaplib import _Authenticator
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required, permission_required

from users.forms import RegisterForm


# Create your views here.

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST[('username')]
        password = request.POST[('password')]
        user = authenticate(request,username=username, password=password)    
        if user is not None:
            login(request, user)
            messages.success(request, 'เข้าสู่ระบบสำเร็จ')
            return redirect('index')
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!')
            return redirect('login')
    else:
        return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    return render(request, 'index.html')

# Logout
def logout_user(request):
    logout(request)
    messages.success(request,'ลงชื่อออกสำเร็จ')
    return redirect('home')


def add_user(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Here1")
            form.save(commit=False)
            form.save()
            print("Here")
            messages.success(request, 'ลงทะเบียนสำเร็จ')
            return redirect('/login/')
        else:
            messages.error(request, 'ลงทะเบียนไม่สำเร็จ')

    return render(request, 'add_user.html', {
        "form": form
        })
