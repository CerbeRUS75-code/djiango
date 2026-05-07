from django import forms

from .models import Author, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "published_year", "price", "author"]
        widgets = {
            "published_year": forms.NumberInput(attrs={"placeholder": "Год издания"}),
            "price": forms.NumberInput(attrs={"step": "0.01"}),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "birth_year"]
        widgets = {
            "birth_year": forms.NumberInput(attrs={"placeholder": "Год рождения"}),
        }
