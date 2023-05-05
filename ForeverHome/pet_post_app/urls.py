from django.urls import path
from pet_post_app import views

urlpatterns = [
    path('search', views.search, name='search'),
    path('liked_posts', views.liked_pet_post, name='liked_posts'),
    path('new_post', views.create_new_post_page, name='new_post'),
    path('details/<str:id>', views.detail_pet_post, name='details'),

]