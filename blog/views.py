from django.shortcuts import render, get_object_or_404
from .models import Blogs

def all_blogs(request):

    blog_count = Blogs.objects.count



    blogs = Blogs.objects.order_by('date')[:2]

    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'total_blogs': blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)

    return render(request, 'blog/detail.html', {'blog': blog})




