from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import Http404
from django.template import loader
from django.utils import timezone

from .models import Comment, Place, Post
from .forms import CommentForm, PostingForm, PlaceForm

# Create your views here.

towns = Place.objects.all()

def index(request):
    if request.method == "GET":
        posts = Post.objects.all()
        template = loader.get_template("posts/index.html")
        context = {
            "all_posts": reversed(list(posts)),
            "all_towns": towns
        }
        return HttpResponse(template.render(context,request))
    else:
        submit = request.POST.get("submit")
        form = PlaceForm(request.POST)
        town = form["town"].value()
        context =Post.objects.filter(place__town = town)
        return render(request,"posts/index.html",{"all_posts":context,"all_towns":towns})

def details(request, id):
    try:
        if request.method == "GET":
            post = Post.objects.get(id = id)
            template = loader.get_template("posts/details.html")
            context = {
                "postDetails":post,
                "currentUser":request.user,
                "authorUser":post.author,
                "comments": Comment.objects.filter(post__id = id)
            }
            return HttpResponse(template.render(context,request))
        else:
            if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = Comment()
                    comment.author = request.user
                    comment.text = form["text"].value()
                    comment.created_date = timezone.now()
                    comment.post_id = id
                    comment.save()
                    return redirect("posts:details",id=id)
    except Post.DoesNotExist:
        raise Http404("Post doesn't exists")
    
    template = loader.get_template("posts/index.html")
    return HttpResponse(template.render({},request))

def create(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostingForm(request.POST,request.FILES)
            if form.is_valid():
                if(request.FILES != 0):
                    post = form.instance
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    return redirect("posts:details",id=post.id)
        else:
            form = PostingForm()
            return render(request,"posts/create.html",{"form":form})
    else:
        return redirect("/admin/login/?next=/posts/create")

def edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #check what state of request is, is user sent data from form
    if request.method == "POST":
        form = PostingForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            post = form.instance
            print(form.instance)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('posts:details', id=post.id)
    else:
        form = PostingForm(instance=post)
    #or he want to edit something
    return render(request, 'posts/edit.html', {'form': form}) 

def error404(request):
    return render(request,"posts/error404.html",{})

def delete(request,id):
    post = get_object_or_404(Post, id=id)
    if post:
        post.delete()
        return redirect("posts:index")
    else:
        content={"errorMessage":"Dany post nie istnieje"}
        return redirect("posts:404",content=content)