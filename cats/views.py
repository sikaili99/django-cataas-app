from django.http import HttpResponse
from django.shortcuts import render
import requests
from .models import Cats

# Home page with showing cats from SQLite db


def index(resquest):

    url = requests.get('https://cataas.com/api/cats?limit=10')
    response = url.json()
    return render(resquest, 'index.html', {'cats': response})


def search(request):
    search_tag = request.GET.get('q')
    if request.method == 'GET' and search_tag != '':

        url = requests.get(f'https://cataas.com/api/cats?tags={search_tag}')
        search_res = url.json()
        print(search_res)
        return render(request, 'search.html', {'results_tag': search_res})

    else:
        return render(request, 'search.html', {'message': 'Enter a tag to search for a cat'})



