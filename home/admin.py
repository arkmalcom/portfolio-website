from django.contrib import admin
from blog.models import Post, Author, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Tag)