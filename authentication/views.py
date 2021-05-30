from django.shortcuts import redirect, render, reverse, HttpResponseRedirect
from authentication.models import Uzer
from authentication.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def Signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = Uzer.objects.create_user(
                username=data['username'], password=data['password'], email=data['email'])
            user.save()
            return HttpResponseRedirect(reverse('login'))
    form = Signup_view()
    return render(request, 'signup.html', {'form': form})


def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    log = logout(request)
    return redirect('home')
