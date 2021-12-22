from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import Http404
from django.template import loader
from django.utils import timezone

from .models import Post
from .forms import PostingForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    template = loader.get_template("posts/index.html")
    context = {
        "all_posts": reversed(list(posts))
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    try:
        post = Post.objects.get(id = id)
        template = loader.get_template("posts/details.html")
        context = {
            "postDetails":post,
            "currentUser":request.user,
            "authorUser":post.author
        }
        return HttpResponse(template.render(context,request))
    except Post.DoesNotExist:
        raise Http404("Post doesn't exists")
    
    template = loader.get_template("posts/index.html")
    return HttpResponse(template.render({},request))

def create(request):

    if request.user.is_authenticated:
        if request.method == "POST":
            form = PostingForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect("details",id=post.id)
        else:
            form = PostingForm()
            return render(request,"posts/create.html",{"form":form})
    else:
        return redirect("/admin/login/?next=/posts/create")

def edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #check what state of request is, is user sent data from form
    if request.method == "POST":
        form = PostingForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
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
