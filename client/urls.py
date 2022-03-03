from django.urls import path
from .views import IndexView, CreateViews,DIndexView,DConforimView,PIndexView,PContractView,PtemplateView,LoginView,DraftViews,SavedViews,DeletedViews,NotificationsViews,DviewhistoryViews
urlpatterns = [
    #mijoz
    path('',IndexView,name='cindex'),
    path('clients/create/',CreateViews,name='ccreate'),
    path('login',LoginView,name='login'),
    path('draft',DraftViews,name='draft'),
    path('csaved',SavedViews,name='csaved'),
    path('cdeleted',DeletedViews,name='cdeleted'),
    path('cnotifications',NotificationsViews,name='cnotifications'),

    #direkotr
    path('direktor/',DIndexView,name='dindex'),
    path('direktor/conforim/',DConforimView,name='dconforim'),
    path('direktor/viewhistory/',DviewhistoryViews,name='viewhistory'),

    #plan adel
    path('plan/',PIndexView,name='pindex'),
    path('plan/contract',PContractView,name='pcontract'),
    path('plan/template',PtemplateView,name='ptemplate'),


    #tekshir
    path('tek/',Tekshir.as_view(),name='Tekshir'),
]
