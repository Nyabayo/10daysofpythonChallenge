from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})