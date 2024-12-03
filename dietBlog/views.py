
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author as the currently logged-in user
            post.save()
            return redirect('post_list')  # Redirect to the list of posts
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if 'update_post' in request.POST:
            form = PostForm(request.POST,  instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user 
                post.save()
                messages.success(request, 'Post updated successfully!')
                return redirect ('dietBlog:post_list')
            else:
                messages.error(request, 'Failed to update post.')
        elif 'delete_post' in request.POST:
            form = PostForm(request.POST,  instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user 
                post.delete()
                messages.success(request, 'Post deleted successfully!')
                return redirect ('dietBlog:post_list')
    else:
        form = PostForm()
    return render(request, 'post_detail.html', {'post': post, 'form': form})