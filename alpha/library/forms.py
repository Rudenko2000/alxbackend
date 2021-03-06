from django import forms
from django.core.exceptions import ValidationError
from .models import Book, Author


class AddBookForm(forms.Form):
    title = forms.CharField(max_length=200)
    author_name = forms.CharField(max_length=200)
    #author=forms.ModelChoiceField(Author.objects.all())

    description = forms.CharField(
        widget=forms.Textarea(attrs={'name':"body, 'rows':3, 'columns'=3"})
    )

    def clean_author_name(self):
        author_name= self.cleaned_data["author_name"]
        if author_name != "Adam Mickewicz":
            raise ValidationError ("Tylko Adam Mickewicz")
        return author_name


class BookForm_ModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','description']

class DeleteBookForm(forms.Form):
    operation = forms.HiddenInput()

class DeleteBookForm(forms.Form):
        operation = forms.CharField(widget=forms.HiddenInput(), required=True, initial="delete")