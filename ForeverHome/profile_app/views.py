from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from profile_app.models import Profile
from pet_post_app.models import Post

from profile_app.forms import RegistrationForm, AccountAuthenticationForm


def home_page(request):
    return render(request, 'profile_app/index.html')


def about_us(request):
    return render(request, 'profile_app/about_us.html')


def personalities(request):
    return render(request, 'profile_app/personalities.html')


def profile(request, *args, **kwargs):
    userID = kwargs.get('userID')
    profile_dict = {}
    try:
        profile = Profile.objects.get(pk=userID)
    except:
        return HttpResponse('That user doesn\'t exist.')

    if profile:
        profile_dict['userID'] = profile.userID
        profile_dict['username'] = profile.username
        profile_dict['email'] = profile.email
        profile_dict['profile_picture'] = profile.profile_picture.url
        profile_dict['posts'] = Post.objects.order_by('id')

    is_self = True
    user = request.user

    if user.is_authenticated and user != profile:
        is_self = False
    elif not user.is_authenticated:
        is_self = False

    profile_dict['is_self'] = is_self

    return render(request, 'profile_app/userprofile.html', context=profile_dict)


def sign_up(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already loged in as {user.username}")
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect("index")

        else:
            context['registration_form'] = form

    return render(request, 'profile_app/sign_up.html', context)


def sign_out(request):
    logout(request)
    return redirect("index")


def sign_in(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("index")

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        print("Got Request!")

        if form.is_valid():
            print("Form is valid")
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                print("Logged in!")
                login(request, user)
                if destination:
                    return redirect(destination)
                return redirect("index")

    else:
        form = AccountAuthenticationForm()

    context['signin_form'] = form

    return render(request, "profile_app/sign_in.html", context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect
