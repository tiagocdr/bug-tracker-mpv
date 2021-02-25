from django.contrib import auth
from django.contrib.auth.backends import RemoteUserBackend
from django.shortcuts import reverse, render, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from myuser.form import LoginForm
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