from django.shortcuts import render

def home(request):
    return render(request, 'dcbsproj/home.html')

def about(request):
    return render(request, 'dcbsproj/about.html')

def contact(request):
    return render(request, 'dcbsproj/contact.html')


# Create your views here.
