from django.shortcuts import render
import requests
my_url = 'https://cataas.com/'


def index(resquest):
    url = requests.get(f'{my_url}api/cats?limit=10')
    response = url.json()

    return render(resquest, 'index.html', {'cats': response})


def search(request):
    search_tag = request.GET.get('q')
    if request.method == 'GET' and search_tag != '':

        url = requests.get(f'{my_url}api/cats?tags={search_tag}')
        search_res = url.json()
        return render(request, 'search.html', {'results_tag': search_res})

    else:
        return render(request, 'search.html', {'message': 'Enter a tag to search for a cat'})
