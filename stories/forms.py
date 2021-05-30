from django.forms import fields, widgets
from stories.models import Book
from django import forms
from stories.models import Book, Chapter


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover']


class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['files']
        widgets = {'files': widgets.ClearableFileInput(
            attrs={'multiple': True})}
