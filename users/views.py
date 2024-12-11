from django.shortcuts import redirect, render
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages, auth


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Вы успешно вошли в аккаунт.")
                return redirect('home')
            else:
                messages.error(request, "Неправильный логин или пароль.")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)




def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)



def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'users/profile.html', context)



def logout(request):
    auth.logout(request)
    messages.success(request, "Вы успешно вышли из системы.")
    return redirect('home')

