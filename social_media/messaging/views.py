from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden

from .models import Conversation, Message
from .forms import MessageForm

User = get_user_model()


@login_required
def inbox(request):
    """
    Display all conversations involving the logged-in user.
    Shows the other user, latest message, and timestamp.
    """
    conversations = request.user.conversations.all().prefetch_related('participants', 'messages')

    conversation_list = []
    for conv in conversations:
        other_user = conv.get_other_user(request.user)
        last_message = conv.get_last_message()
        if other_user:
            conversation_list.append({
                'conversation': conv,
                'other_user': other_user,
                'last_message': last_message,
            })

    # Sort conversations by latest message timestamp (newest first)
    conversation_list.sort(
        key=lambda x: x['last_message'].created_at if x['last_message'] else x['conversation'].created_at,
        reverse=True
    )

    return render(request, 'messaging/inbox.html', {
        'conversation_list': conversation_list,
    })


@login_required
def chat(request, username):
    """
    1-to-1 chat view between logged-in user and another user.
    Reuses an existing conversation or creates one if it does not exist.
    """
    other_user = get_object_or_404(User, username=username)

    # Prevent users from messaging themselves
    if request.user == other_user:
        return redirect('inbox')

    # Find existing conversation between both users or create a new one
    conversation = Conversation.objects.filter(
        participants=request.user
    ).filter(
        participants=other_user
    ).first()

    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)

    # Mark incoming messages as read when opening the conversation
    conversation.messages.filter(sender=other_user, is_read=False).update(is_read=True)

    # Handle sending a new message
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            return redirect('chat', username=other_user.username)
    else:
        form = MessageForm()

    messages = conversation.messages.all()

    return render(request, 'messaging/chat.html', {
        'conversation': conversation,
        'other_user': other_user,
        'chat_messages': messages,
        'form': form,
    })
