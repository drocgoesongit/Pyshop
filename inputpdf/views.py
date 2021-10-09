from django.shortcuts import render, redirect, HttpResponse
from .models import Staff, Resumes
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'getStarted.html')


def home(request):
    if request.method == "POST":
        files = request.FILES["files"]

        document = Resumes.objects.create(file=files)
        document.save()
        return redirect('parserOutput')


    return render(request, 'home.html')


def getStarted(request):
    return render(request, 'getStarted.html')


def loginPage(request):
    if request.method == 'POST':
        userName = request.POST.get('username'),
        passWord = request.POST.get('password')

        user = authenticate(request, username=userName, password=passWord)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password incorrect")

    context = {}
    return render(request, "login.html", context)


def register(request):
    # if request.user.is_authenticated:
    #     return redirect('')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.active = True
            user.staff = False
            user.admin = False
            user.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, "register.html", context)


def parser(request):
    return render(request, 'parserPage.html')
