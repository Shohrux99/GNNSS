from django.shortcuts import render


def IndexView(request):


    return render(request,'main/index.html')

def CreateViews(request):


    return render(request,'main/create.html')
    

def DIndexView(request):


    return render(request,'direktor/index.html')

def DConforimView(request):


    return render(request,'direktor/history.html')
def PIndexView(request):


    return render(request,'plan/index.html')
def PContractView(request):


    return render(request,'plan/template.html')

def PtemplateView(request):


    return render(request,'plan/template.html')
def LoginView(request):


    return render(request,'main/login.html')