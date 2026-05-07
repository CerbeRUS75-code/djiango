from django.shortcuts import redirect, render

from .forms import AuthorForm, BookForm
from .models import Book


def index(request):
    books = Book.objects.select_related("author").all()
    return render(request, "index.html", {"books": books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = BookForm()

    return render(request, "add_book.html", {"form": form})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AuthorForm()

    return render(request, "add_author.html", {"form": form})
