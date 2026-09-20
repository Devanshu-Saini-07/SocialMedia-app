from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    """
    Simple form for sending a text message.
    """
    class Meta:
        model = Message
        fields = ["content"]
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "class": "form-control me-2",
                    "placeholder": "Type a message...",
                    "autocomplete": "off",
                    "required": True,
                }
            )
        }
        labels = {
            "content": "",
        }
