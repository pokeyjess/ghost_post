from django.shortcuts import render, HttpResponseRedirect, reverse
from ghost_post_app.models import Posts
from ghost_post_app.forms import PostForm

def index(request):
    post_list = Posts.objects.all().order_by('-post_time')
    return render(request, "index.html", {"post_list": post_list, "hello": "Boast or Roast"})

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Posts.objects.create(boast_or_roast=data['choice'], content=data['content'], up_votes=0, down_votes=0)
            return HttpResponseRedirect(reverse('homepage'))
        
    form = PostForm()
    return render(request, "post_form.html", {"form": form})

def boast(request):
    post_list = Posts.objects.filter(boast_or_roast=True).order_by('-post_time')
    return render(request, "index.html", {"post_list": post_list})

def roast(request):
    post_list = Posts.objects.filter(boast_or_roast=False).order_by('-post_time')
    return render(request, "index.html", {"post_list": post_list})

def up_vote(request, post_id):
    vote = Posts.objects.get(id=post_id)
    vote.up_votes += 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage')) 

def down_vote(request, post_id):
    vote = Posts.objects.get(id=post_id)
    vote.down_votes += 1
    vote.save()
    return HttpResponseRedirect(reverse('homepage'))

