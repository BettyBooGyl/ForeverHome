from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from profile_app.forms import RegistrationForm


def home_page(request):
    return render(request, 'profile_app/index.html')
def about_us(request):
    return render(request, 'profile_app/about_us.html')
def personalities(request):
    return render(request, 'profile_app/personalities.html')
def profile(request):
    return render(request, 'profile_app/userprofile.html')
def sign_in(request):
    return render(request, 'profile_app/sign_in.html')
def sign_up(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already loged in as {user.username}")
    context ={}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get("next")
            if destination:
                return redirect(destination)
            return redirect("index")
        
        else:
            context['registration_form'] = form

    return render(request, 'profile_app/sign_up.html', context)