from django import forms


class SearchForm(forms.Form):
    """
    Form for searching users and posts via GET request.
    """
    query = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Search users or posts...",
                "autocomplete": "off",
            }
        ),
    )
