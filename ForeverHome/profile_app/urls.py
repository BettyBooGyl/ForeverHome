from django.urls import path
from profile_app import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('personalities', views.personalities, name='personalities'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('userprofile', views.profile, name='userprofile'),
    

]