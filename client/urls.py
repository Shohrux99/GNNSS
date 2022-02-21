
from django.urls import path
from .views import IndexView, CreateViews
urlpatterns = [
    path('',IndexView,name='index'),
    path('create',CreateViews,name='create'),

]
