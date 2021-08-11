from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def projects(request):
    return render(request, 'home/projects.html')

def blog(request):
    return render(request, 'home/blog.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')