from django.urls import path
from profile_app import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('personalities', views.personalities, name='personalities'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('userprofile', views.profile, name='userprofile'),

]