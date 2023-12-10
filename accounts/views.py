from django.shortcuts import render, redirect
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout, decorators
from accounts.forms import UserAcountLoginForm, UserAccountRegisterForm
from django.contrib.auth.models import User


def user_login(request):
    next = request.GET.get('next')
    print(request.user)
    print(request.user.is_authenticated)
    print(request.method)

    if request.method == 'GET':
        loginForm = UserAcountLoginForm()
    else:
        loginForm = UserAcountLoginForm(data=request.POST)
        if loginForm.is_valid():
            # print(f"is valid: {loginForm.is_valid()}")
            print(loginForm.cleaned_data)

            user_name = loginForm.cleaned_data.get('username')
            user_password = loginForm.cleaned_data.get('password')
            user = authenticate(request, username=user_name, password=user_password)
            if user is not None:
                print('ok')
                print(f"before login {request.user.is_authenticated}")

                login(request, user)

                print(f"after login {request.user.is_authenticated}")
                
                if next:
                    return redirect(next)
                else:
                    return redirect("blog:blog_page")
            else:
                print('nok')
                loginForm.add_error('password', "رمز یا نام اشتب")
                # loginForm.add_error('username',"نام کاربری  اشتب")

    print(request.method)
    return render(request, "accounts/login.html", {'form': loginForm})


def user_logout(request):
    print(request.user)

    logout(request)

    print(request.user)
    return redirect("blog:blog_page")


def user_register(request):
    if request.user.is_authenticated:
        return redirect('blog:blog_page')
    print(request.method)
    if request.method == 'GET':
        registerForm = UserAccountRegisterForm()
    else:
        registerForm = UserAccountRegisterForm(data=request.POST)
        if registerForm.is_valid():
            # print(f"is valid: {registerForm.is_valid()}")
            print(registerForm.cleaned_data)
            first_name = registerForm.cleaned_data['first_name']
            last_name = registerForm.cleaned_data.get('last_name')
            email = registerForm.cleaned_data.get('email')
            username = registerForm.cleaned_data.get('username')
            password_2 = registerForm.cleaned_data.get('password_2')

            regUser = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password_2)
            print("create user")
            return redirect('accounts:login_page')

    context = {
        'form': registerForm
    }
    return render(request, "accounts/user.html", context)
