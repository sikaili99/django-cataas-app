from django.urls import path
from cats import views  # Import view from the current folder

# Here I have created routes of the app
urlpatterns = [
    path('', views.index, name='index'),
    path('search/result', views.search,  name='search'),
    path('view/cat/<cat_id>', views.view_cat, name='view_cat')
]
