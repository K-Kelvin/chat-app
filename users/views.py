from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import PasswordResetView as PRV
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
from .forms import UserRegisterForm

@login_required
def index(request):
    ''' Home view '''
    return redirect('chat:index')

# Register members
def register(request):
    ''' Handle registration logic '''
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}, you can now login')
            return redirect('users:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    err_msg = error.capitalize()
                    messages.error(request, err_msg)
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('chat:index')
    context = {'form': form}
    return render(request, "register.html", context)

# Allow people to signIn
def login(request):
    ''' Handle login logic '''
    username = ''
    password = ''
    if request.method == 'POST':
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('chat:index')
        else:
            messages.error(request, 'Username or Password is incorrect')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('chat:index')
    context = {'username':username, 'password':password}
    return render(request, "login.html", context)

class PasswordResetView(PRV):
    ''' View to help in password reset '''
    from_email = settings.HELP_EMAIL
