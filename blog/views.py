from django.shortcuts import render
from .models import Author, Tag, Post
from django.views.generic import ListView, DetailView

# Create your views here.
class BlogView(ListView):
    paginate_by = 4
    model = Post
    fields = "__all__"
    template_name = "blog/blog.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["posts"] = Post.objects.all()
        return context

class PostView(DetailView):
    model = Post
    template_name = "blog/post.html"

def blog_category_view(request, tag_filter, description_slug):
    filtered_posts = Post.objects.all().filter(tag__id=tag_filter)
    context = { 'page_obj' : filtered_posts }
    return render(request, 'blog/blog.html', context)