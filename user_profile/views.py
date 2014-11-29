from django.shortcuts import render

# Create your views here.

from .forms import UserCreationEmailForm, EmailAuthenticationForm


def signup(request):
    form = UserCreationEmailForm(request.POST or None)

    if form.is_valid():
        form.save()
    #logear el usuario
    #crear user profile

    return render(request, 'signup.html', {'f': form})


def signin(request):
    form = EmailAuthenticationForm(request.POST or None)

    return render(request, 'signin.html', {'f': form})

