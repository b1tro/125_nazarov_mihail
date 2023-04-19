from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def categoriesView(request, category_id):
    return HttpResponse(f"<h1>Начальная страница приложения categories</h1><p>{category_id}</p>")

def publicationsView(request):
    return HttpResponse("Это начальная страница приложения publications")

def startView(request):
    return render(request, 'publications/index.html')

def requestView(request):
    if request.GET:
        print(request.GET)
    else:
        return HttpResponse("No request")
def aboutView(request):
    return render(request, 'publications/about.html')
def pageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена!")