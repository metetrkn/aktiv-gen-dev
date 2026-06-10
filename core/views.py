from django.shortcuts import render
from .models import Post

def post_list(request):
    # Fetch all posts, ordered by the newest first
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'core/post_list.html', {'posts': posts})
