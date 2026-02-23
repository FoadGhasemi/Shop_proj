from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm, ProfileEditForm
from django.contrib import messages
from product.models import Product


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        print('Post')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('Valid')
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            # Check passwords manually
            if password1 != password2:
                messages.error(request, "Passwords do not match.")
                return render(request, 'user/auth-register-basic.html', {'form': form})
            print('Matched')
            user = form.save()
            print('Saved')
            login(request, user)

            return redirect('home:home')

    else:
        form = UserRegisterForm()

    return render(request, 'user/auth-register-basic.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home:home')

    else:
        form = UserLoginForm()

    return render(request, 'user/auth-login-basic.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':

        # instance=profile -> updates an existing user not making a new one

        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'user/profile.html', {'form': form})


