from django.shortcuts import render

def home(request):
    return render(request, 'dcbsproj/home.html', {'title':'Welcome'})

def about(request):
    return render(request, 'dcbsproj/about.html', {'title':'Welcome'})

def contact(request):
    return render(request, 'dcbsproj/contact.html', {'title':'Welcome'})


# Create your views here.
