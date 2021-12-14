from django.http import HttpResponse
from django.http.response import Http404
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    template = loader.get_template("posts/index.html")
    context = {
        "all_posts":posts
    }
    return HttpResponse(template.render(context,request))

def details(request, id):
    try:
        post = Post.objects.get(id = id)
        template = loader.get_template("posts/details.html")
        context = {
            "postDetails":post
        }
        return HttpResponse(template.render(context,request))
    except Post.DoesNotExist:
        raise Http404("Post doesn't exists")
    
    template = loader.get_template("posts/index.html")
    return HttpResponse(template.render({},request))