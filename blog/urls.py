from django.urls import path;
from . import views;

urlpatterns = [
    path('', views.BlogView.as_view(), name="blog"),
    path('<int:pk>/<title>', views.PostView.as_view(), name="post"),
]