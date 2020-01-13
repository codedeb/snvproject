
from .models import UserModel
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from.forms import RegistrationForm, LoginForm

# Create your views here.


def registrationView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Your account has successfully created')
            return redirect('login')  # redirecting to login.html

    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def logingView(request):
    user = request.user
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Welcome you are logged in')
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})  # it takes us to login page'


def homeView(request):
    obj = UserModel.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'accounts/home.html', context)
