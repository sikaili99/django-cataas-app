from django.shortcuts import render
from random import choice


def index(resquest):
    random_tags = choice(['cute', 'hello', 'beautiful', 'Programmer', 'codes'])

    # Random urls are generated here
    url_list = ['https://cataas.com/cat',
               'https://cataas.com/cat/cute',
               'https://cataas.com/cat/gif',
               f'https://cataas.com/cat/cute/says/{random_tags}',
               f'https://cataas.com/cat/{random_tags}/says/{random_tags}'
               ]
    url = choice(url_list)

    return render(resquest, 'index.html', {'image_url': url})


def search(request):
    search_tag = request.GET.get('q')
    if request.method == 'GET' and search_tag != '':

        return render(request, 'search.html', {'tag': search_tag})

    else:
        return render(request, 'search.html', {'message': 'Enter a tag to search for a cat'})
