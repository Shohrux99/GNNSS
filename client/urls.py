
from django.urls import path
from .views import IndexView, CreateViews, LoginView
urlpatterns = [
    path('',IndexView,name='index'),
    path('create',CreateViews,name='create'),
    path('login',LoginView,name='login'),

]
