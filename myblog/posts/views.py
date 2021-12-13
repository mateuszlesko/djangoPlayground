from django.http import HttpResponse
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