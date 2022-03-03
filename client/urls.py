from django.urls import path
from .views import IndexView, CreateViews,DIndexView,DConforimView,PIndexView,PContractView,PtemplateView,LoginView
from .apiview import Tekshir


urlpatterns = [
    #mijoz
    path('',IndexView,name='cindex'),
    path('clients/create/',CreateViews,name='ccreate'),
    path('login',LoginView,name='login'),
    #direkotr
    path('direktor/',DIndexView,name='dindex'),
    path('direktor/conforim/',DConforimView,name='dconforim'),

    #plan adel
    path('plan/',PIndexView,name='pindex'),
    path('plan/contract',PContractView,name='pcontract'),
    path('plan/template',PtemplateView,name='ptemplate'),


    #tekshir
    path('tek/',Tekshir.as_view(),name='Tekshir'),
]
