from django import forms
from website.models import Contact, NewsLetters


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=300)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        exclude = ['created_date', 'updated_date']


class NewsLettersForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = NewsLetters
        fields = '__all__'
