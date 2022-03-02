
from django.urls import path
<<<<<<< HEAD
from .views import IndexView, CreateViews,DIndexView,DConforimView,PIndexView,PContractView,PtemplateView
urlpatterns = [
    #mijoz
    path('',IndexView,name='cindex'),
    path('clients/create/',CreateViews,name='ccreate'),
    #direkotr
    path('direktor/',DIndexView,name='dindex'),
    path('direktor/conforim/',DConforimView,name='dconforim'),
=======
from .views import IndexView, CreateViews, LoginView
urlpatterns = [
    path('',IndexView,name='index'),
    path('create',CreateViews,name='create'),
    path('login',LoginView,name='login'),
>>>>>>> 0a56b89a8570973311700f4fc4081b07b63a669e

    #plan adel
    path('plan/',PIndexView,name='pindex'),
    path('plan/contract',PContractView,name='pcontract'),
    path('plan/template',PtemplateView,name='ptemplate'),
]
