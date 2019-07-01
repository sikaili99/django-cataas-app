from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Cats

# Home page with showing cats from SQLite db


def index(resquest):

    cats = Cats.objects.all()
    return render(resquest, 'index.html', {'cats': cats})


def search(request):
    search_tag = request.GET.get('q')
    if request.method == 'GET' and search_tag != '':

        return render(request, 'search.html', {'tag': search_tag})

    else:
        return render(request, 'search.html', {'message': 'Enter a tag to search for a cat'})



