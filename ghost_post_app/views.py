from django.shortcuts import render
from ghost_post_app.models import Posts
from ghost_post_app.forms import PostForm

def index(request):
    return render(request, "index.html", {"hello": "Hello"})

def post_form_view(request):
    form = PostForm()
    return render(request, "post_form.html", {"form": form})