from django.urls import path
from pet_post_app import views

urlpatterns = [
    path('search', views.search, name='search'),
    path('liked_posts', views.liked_pet_post, name='liked_posts'),
    path('new_post', views.create_new_post_page, name='new_post'),
    path('details', views.detail_pet_post, name='details'),
    
    #searchthings -kylynn
        path('pet/<str:slug>/<int:id>', views.pet_detail, name='pet_detail'),
        path('filter-data', views.filter_data, name='filter_data'),


]