from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from social_media.posts.models import Post


@login_required
def home(request):
    """Home feed showing all posts, newest first, with optimized queries."""
    # Fetch posts with author and annotate with counts in a single query
    posts = Post.objects.all().select_related('author').annotate(
        like_count=Count('likes'),
        comment_count=Count('comments')
    )

    # Build the context with user's like status
    posts_with_counts = []
    for post in posts:
        user_has_liked = False
        if request.user.is_authenticated:
            user_has_liked = post.likes.filter(user=request.user).exists()
        posts_with_counts.append({
            'post': post,
            'like_count': post.like_count,
            'comment_count': post.comment_count,
            'user_has_liked': user_has_liked,
        })

    return render(request, "feed/home.html", {'posts_with_counts': posts_with_counts})
