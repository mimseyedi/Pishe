from django import forms
from bookstore.models import BookComment

class BookCommentForm(forms.ModelForm):

    class Meta:
        model = BookComment
        fields = "__all__"