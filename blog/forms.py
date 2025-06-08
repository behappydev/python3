from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model  = Author
        fields = ["name", "bio"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model  = Category
        fields = ["name", "description"]

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ["title", "content", "author", "category"]

class SearchForm(forms.Form):
    query = forms.CharField(label="Buscar post", max_length=100)
