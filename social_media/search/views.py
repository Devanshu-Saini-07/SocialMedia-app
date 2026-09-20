from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from social_media.posts.models import Post
from .forms import SearchForm

User = get_user_model()


@login_required
def search(request):
    """
    Search view for users and posts.
    Accepts a GET query parameter and performs case-insensitive search.
    """
    query = request.GET.get('query', '').strip()[:255]
    users = []
    posts = []

    if query:
        # Search users by username (case-insensitive)
        users = User.objects.filter(username__icontains=query)

        # Search posts by content (case-insensitive)
        # Use select_related to avoid N+1 queries when fetching post authors
        posts = Post.objects.filter(content__icontains=query).select_related('author')

    form = SearchForm(initial={'query': query})

    context = {
        'form': form,
        'query': query,
        'users': users,
        'posts': posts,
    }

    return render(request, 'search/search.html', context)
