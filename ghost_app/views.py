from django.shortcuts import render, redirect
from ghost_app.forms import PostForm
from ghost_app.models import Posts
from django.http import HttpResponseRedirect

# Create your views here.
def index_view(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request,'index.html',{'posts': posts})

def submit_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            Posts.objects.create(
            text = data['text'],
            post_type = data['post_type'],
            )
    form = PostForm()
    return render(request,'submit.html',{'form': form})

def sorted_view(request):
    posts = Posts.objects.all().order_by('-likes')
    return render(request,'sorted.html', {'posts':posts})

def boasts_view(request):
    posts = Posts.objects.filter(post_type=True).order_by('-created_at')
    return render(request,'boasts.html', {'posts':posts})
    # THIS IS THE VIEW FOR BOASTS ONLY

def roasts_view(request):
    posts = Posts.objects.filter(post_type=False).order_by('-created_at')
    return render(request,'roasts.html', {'posts':posts})
    # THIS IS THE VIEW FOR ROASTS ONLY

def likes_view(request,post_id):
    post = Posts.objects.filter(id=post_id).first()
    post.likes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def dislikes_view(request,post_id):
    post = Posts.objects.filter(id=post_id).first()
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))