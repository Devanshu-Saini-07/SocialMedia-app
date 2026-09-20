from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Simple form for creating comments."""

    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write a comment...',
            }),
        }
        labels = {
            'content': '',  # No label needed
        }
