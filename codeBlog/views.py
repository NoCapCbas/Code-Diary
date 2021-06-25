from django.shortcuts import render
from .models import Post



# Create your views here.
def index(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'codeBlog/index.html', context)

def about(request):
    context = {}
    return render(request, 'codeBlog/about.html', context)
