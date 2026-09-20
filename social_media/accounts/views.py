from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup_view(request):
    """
    Handle user registration.
    GET  → show the empty signup form.
    POST → validate, create the user, log them in, redirect to home.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)          # auto-login after signup
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """
    Handle user login.
    GET  → show the login form.
    POST → authenticate, log in, redirect to home (or show error).
    """
    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."

    return render(request, 'accounts/login.html', {'error_message': error_message})


def logout_view(request):
    """Log the user out and redirect to the login page."""
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    """Show the logged-in user's profile page."""
    return render(request, 'accounts/profile.html', {'profile_user': request.user})


def user_profile_view(request, username):
    """Show another user's profile page."""
    from django.contrib.auth import get_user_model
    User = get_user_model()
    from django.shortcuts import get_object_or_404
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'accounts/profile.html', {'profile_user': profile_user})
