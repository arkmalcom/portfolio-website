from django.shortcuts import render
from .models import Author, Tag, Post
from django.views.generic import TemplateView, DetailView

# Create your views here.
class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["posts"] = Post.objects.all()
        return context

class PostView(DetailView):
    model = Post
    template_name = "blog/post.html"