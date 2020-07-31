from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from .form import RegisterForm


class Login(LoginView):
    template_name = 'loginsys/login.html'


class Logout(LogoutView):
    next_page = '/'



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password2'])
            auth.login(request, user)
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'loginsys/register.html', {'form': form})
