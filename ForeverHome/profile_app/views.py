from django.shortcuts import render

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
def sign_up(request):
    return render(request, 'profile_app/sign_up.html')