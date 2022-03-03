from django.shortcuts import render


def IndexView(request):


    return render(request,'main/index.html')

def CreateViews(request):


    return render(request,'main/create.html')

def DraftViews(request):


    return render(request,'main/draft.html')

def SavedViews(request):


    return render(request,'main/saved.html')

def DeletedViews(request):


    return render(request,'main/deleted.html')

def NotificationsViews(request):


    return render(request,'main/notifications.html')

def DIndexView(request):


    return render(request,'direktor/index.html')

def DConforimView(request):


    return render(request,'direktor/history.html')

def DviewhistoryViews(request):


    return render(request,'direktor/viewhistory.html')

def PIndexView(request):


    return render(request,'plan/index.html')

def PContractView(request):


    return render(request,'plan/template.html')

def PtemplateView(request):


    return render(request,'plan/template.html')

def LoginView(request):


    return render(request,'main/login.html')