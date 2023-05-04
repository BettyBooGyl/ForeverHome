from django.shortcuts import render
from pet_post_app.models import Post


def search(request):
    return render(request, 'pet_post_app/browsing_page.html')


def create_new_post_page(request):
    return render(request, 'pet_post_app/create_new_post.html')


def detail_pet_post(request):
    return render(request, 'pet_post_app/detail_pet_post.html')


def liked_pet_post(request):
    post_list = Post.objects.order_by('id')
    post_dict = {'liked_posts': post_list}
    return render(request, 'pet_post_app/liked_pet_post.html', context=post_dict)
