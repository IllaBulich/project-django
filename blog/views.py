from django.shortcuts import render
from blog.models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(
        request, 
        'blog/about.html',
        {
            'title':'About',
        }
    )