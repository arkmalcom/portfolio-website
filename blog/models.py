from django.db import models
from ckeditor.fields import RichTextField

languages = [
    ("ES", "Español"),
    ("EN", "English"),
]

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Tag(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    date_published = models.DateField(auto_now_add=True)
    repo_link = models.CharField(max_length=255, blank=True, null=True)
    banner_img = models.CharField(max_length=255, blank=True, null=True)
    lang = models.CharField(max_length=2, choices=languages, default="EN")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title

    def get_tags(self):
        tags = [tag.description for tag in self.tag.all()]
        return tags
