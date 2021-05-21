
from django.contrib import auth
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import redirect, reverse, render, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from myuser.form import LoginForm, SignUpForm
from myuser.models import MyUser
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'form.html', {'form':form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                    )
            
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

    
def logout_view(request):
    logout(request)
    return redirect('home')
