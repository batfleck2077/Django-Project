from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, 'frontpage.html',{})

def login(request):
    return render(request,'registration/login.html',{})

def index(request):
        return render(request,'index.html',{})
    
def forms(request):
    return render(request,'forms.html',{})