from django.urls import path;
from . import views;

urlpatterns = [
    path('', views.BlogView.as_view(), name="blog"),
    path('category/<str:tag_filter>/<slug:description_slug>', views.blog_category_view, name="blog-category"),
    path('<int:pk>/<title>', views.PostView.as_view(), name="post"),
]