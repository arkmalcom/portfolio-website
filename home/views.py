from django.shortcuts import render
from blog.models import Post
from projects.models import Project

# Create your views here.
def home(request):
    context = {}
    context["projects"] = Project.objects.all()
    context["posts"] = Post.objects.all()
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')