from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

def search(request):
    return render(request, 'pet_post_app/browsing_page.html')


def create_new_post_page(request):
    return render(request, 'pet_post_app/create_new_post.html')


def detail_pet_post(request, id):
    post_list = Post(id)
    return render(request, 'pet_post_app/detail_pet_post.html', context={"id": id})


def liked_pet_post(request):
    return render(request, 'pet_post_app/liked_pet_post.html')

#filter search things-kylynn
def pet_detail(request,slug,id):
	pet=Pet.objects.get(id=id)
	related_pets=Pet.objects.filter(category=pet.category).exclude(id=id)[:4]
	return render(request, 'browsing_page.html',{'data':pet,'related':related_pets,'breeds':breed,'sizes':size,'personalitys':personalitys,'ages':ages})

def search(request):
	q=request.GET['q']
	data=Pet.objects.filter(title__icontains=q).order_by('-id')
	return render(request,'search.html',{'data':data})

def filter_data(request):
	breeds=request.GET.getlist('breed[]')
	ages=request.GET.getlist('age[]')
	personalitys=request.GET.getlist('personality[]')
	sizes=request.GET.getlist('size[]')
	
	allPets=Pet.objects.all().order_by('-id').distinct()
	if len(breeds)>0:
		allPets=allPets.filter(petattribute__breeds__id__in=breeds).distinct()
	if len(ages)>0:
		allPets=allPets.filter(ages__id__in=ages).distinct()
	if len(personalitys)>0:
		allPets=allPets.filter(personalitys__id__in=personalitys).distinct()
	if len(sizes)>0:
		allPets=allPets.filter(petattribute__size__id__in=sizes).distinct()
	t=render_to_string('ajax/browsing_page.html',{'data':allPets})
	return JsonResponse({'data':t})
