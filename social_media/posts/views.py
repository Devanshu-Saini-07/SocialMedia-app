from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Count

from .models import Post
from .forms import PostForm
from social_media.interactions.forms import CommentForm


@login_required
def create_post(request):
    """Show the create-post form (GET) and save a new post (POST)."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)   # don't save to DB yet
            post.author = request.user       # attach the logged-in user as author
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


def post_detail(request, pk):
    """Show a single post with likes and comments."""
    # Fetch post with author and annotate with counts in a single query
    post = get_object_or_404(
        Post.objects.select_related('author').annotate(
            like_count=Count('likes'),
            comment_count=Count('comments')
        ),
        pk=pk
    )

    # Get like count and check if current user has liked it
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = post.likes.filter(user=request.user).exists()

    # Get comments for this post with user data
    comments = post.comments.all().select_related('user').order_by('created_at')

    context = {
        'post': post,
        'like_count': post.like_count,
        'user_has_liked': user_has_liked,
        'comments': comments,
        'comment_count': post.comment_count,
        'comment_form': CommentForm(),
    }
    return render(request, 'posts/post_detail.html', context)


@login_required
def edit_post(request, pk):
    """Let the author edit their post; block everyone else."""
    post = get_object_or_404(Post, pk=pk)

    # Only the author is allowed to edit
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, pk):
    """Let the author delete their post; block everyone else."""
    post = get_object_or_404(Post, pk=pk)

    # Only the author is allowed to delete
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    # Show a confirmation page on GET
    return render(request, 'posts/delete_post.html', {'post': post})
