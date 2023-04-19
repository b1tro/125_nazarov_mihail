from django.urls import path

from .views import *

urlpatterns = [
    path('publications/',publicationsView),
    path('categories/<int:category_id>/', categoriesView),
    path('',startView),
    path('request/', requestView),
    path('about/', aboutView)
]

