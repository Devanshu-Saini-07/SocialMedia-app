from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Count, Exists, OuterRef

from social_media.posts.models import Post
from .models import Like, Comment
from .forms import CommentForm


@login_required
def toggle_like(request, post_id):
    """
    Toggle like on a post.
    If the user has already liked it, unlike it.
    If not, create a new like.
    """
    if request.method != 'POST':
        return HttpResponseForbidden("Only POST requests are allowed.")

    post = get_object_or_404(Post, pk=post_id)

    # Check if the user has already liked this post
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        # Unlike: delete the existing like
        like.delete()
    else:
        # Like: create a new like
        Like.objects.create(user=request.user, post=post)

        # Create notification only if liking someone else's post
        if post.author != request.user:
            from social_media.notifications.models import Notification
            Notification.objects.create(
                recipient=post.author,
                sender=request.user,
                notification_type='like',
                post=post
            )

    # Redirect back to where the user came from
    next_url = request.POST.get('next', 'home')
    if next_url == 'post_detail':
        return redirect('post_detail', pk=post.pk)
    return redirect('home')


@login_required
def add_comment(request, post_id):
    """Add a comment to a post."""
    if request.method != 'POST':
        return HttpResponseForbidden("Only POST requests are allowed.")

    post = get_object_or_404(Post, pk=post_id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

        # Create notification only if commenting on someone else's post
        if post.author != request.user:
            from social_media.notifications.models import Notification
            Notification.objects.create(
                recipient=post.author,
                sender=request.user,
                notification_type='comment',
                post=post
            )

    # Redirect back to the post detail page
    return redirect('post_detail', pk=post.pk)


@login_required
def delete_comment(request, comment_id):
    """Delete a comment. Only the comment's author can delete it."""
    if request.method != 'POST':
        return HttpResponseForbidden("Only POST requests are allowed.")

    comment = get_object_or_404(Comment, pk=comment_id)

    # Security check: only the comment author can delete it
    if comment.user != request.user:
        return HttpResponseForbidden("You cannot delete another user's comment.")

    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk=post_pk)
