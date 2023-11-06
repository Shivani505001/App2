from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('article/',views.search_view,name='search'),
    path('article/<int:id>/',views.article_view,name='homes'),
    path('article/create',views.create_view,name='create')
]
