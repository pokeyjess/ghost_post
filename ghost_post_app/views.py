from django.shortcuts import render, HttpResponseRedirect, reverse
from ghost_post_app.models import Posts
from ghost_post_app.forms import PostForm

def index(request):
    post_list = Posts.objects.all().order_by('-post_time')
    return render(request, "index.html", {"post_list": post_list, "hello": "Hello"})

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posts.objects.create(boast_or_roast=data['choice'], content=data['content'], up_votes=0, down_votes=0)
            return HttpResponseRedirect(reverse('homepage'))
        
    form = PostForm()
    return render(request, "post_form.html", {"form": form})