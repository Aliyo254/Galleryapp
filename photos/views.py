from django.shortcuts import render
from .models import Image


# Create your views here.
def index(request):
    images = Image.objects.all()
    print (images)
    return render(request, 'photos/index.html', {'images': images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        print(searched_images)
        return render(request, 'photos/results.html', {"message": message, "images": searched_images})