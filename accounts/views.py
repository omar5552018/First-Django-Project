from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, UpdateInfoForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request):
    args = dict(user=request.user)
    return render(request, 'accounts/home.html', args)

def login_redirect(request):
    return HttpResponse(reverse('login'))

def register(request):
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse('login')) 
    else:
        form = RegistrationForm()

        args = dict(form=form)
        return render(request, 'accounts/register.html', args)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
        args = dict(user=user)
        return render(request, 'accounts/other_profile.html', args)
    else:
        user = request.user
        args = dict(user=user)
        return render(request, 'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method=='POST':
        form = UpdateInfoForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('/accounts/profile')
    else:
        form = UpdateInfoForm(instance=request.user)
        args = dict(form=form)
        return render(request, 'accounts/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:           
            return redirect('/accounts/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)



