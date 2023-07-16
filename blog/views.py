from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required 

posts = [
      {
      'author':'CoreyMS',
      'title':'Blog Post 1',
      'content':'First post content',
      'date_posted': 'August 27, 2018',
      },
      
      {
      'author':'Jane Doe',
      'title':'Blog Post 2',
      'content':'second post content',
      'date_posted': 'August 27, 2018',
      },
      {
      'author':'CoreyMS',
      'title':'Blog Post 3',
      'content':'third post content',
      'date_posted': 'August 27, 2018',
      },
]





# Create your views here.
@login_required
def home(request):
    context = {
            # 'posts': posts,
            'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html' , context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})


