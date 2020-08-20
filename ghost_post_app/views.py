from django.shortcuts import render
from ghost_post_app.models import Posts

def index(request):
    return render(request, "index.html", {"hello": "Hello"})
