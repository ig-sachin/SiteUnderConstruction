from django.shortcuts import render

# Create your views here.

def home(request):
    print("I am home view")
    return render(request, 'home.html')

def about(request):
    print("I am about view")
    return render(request, 'about.html')