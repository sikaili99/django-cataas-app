from django.shortcuts import render
import requests
my_url = 'https://cataas.com/'


def index(resquest):
    # Get first 9 cats on the home page
    response = requests.get(f'{my_url}api/cats?limit=9').json()
    
    return render(resquest, 'index.html', {'cats': response})


def search(request):
    search_tag = request.GET.get('q')
    if request.method == 'GET' and search_tag != '':

        url = requests.get(f'{my_url}api/cats?tags={search_tag}')
        search_result = url.json()
        not_found = f"No cat found with your tag key word '{search_tag}'"
        if search_result:
            return render(request, 'search.html', {'results_tag': search_result})
        
        return render(request, 'search.html', {'message': not_found})

    else:
        return render(request, 'search.html', {'message': 'Enter a tag to search for a cat, e.g Jump'})


def view_cat(request, cat_id):

    cat_url = f'{my_url}cat/{cat_id}'
    return render(request, 'view_cat.html', {'view_cat': cat_url})

