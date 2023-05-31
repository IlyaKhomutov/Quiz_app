from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib import messages


def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get("first_name")
            lastname = form.cleaned_data.get("last_name")
            messages.success(request, f"{firstname} {lastname}'s account was created")
            return redirect('accounts:register')

    context = {'form': form}
    return render(request, 'accounts/register2.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('quizzes:main-view')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('quizzes:main-view')
        else:
            messages.info(request, "Sorry, we can't find an account with these credentials.")
    return render(request, 'accounts/login2.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
