from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        "books": Book.objects.all(),
    }
    return render(request, "index.html", context)

# ---------------Handle Book Data--------------------------------------

def add_book(request):
    Book.objects.create(
        title = request.POST['title_input'],
        desc = request.POST['book_desc']
    )
    return redirect("/")

def view_book(request, book_id):
    book = Book.objects.get(id = book_id)
    context = {
        "book": book,
        "authors": Author.objects.exclude(books=book.id)
    }
    return render(request, "book_view.html", context)

def add_author_to_book(request, book_id):
    book = Book.objects.get(id = book_id)
    book.authors.add(Author.objects.get(id=request.POST['author_select']))
    return redirect(f"/books/{book.id}")

# ---------------End Book Handling-----------------------------------
# ---------------Handle Author Data----------------------------------

def author_index(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "author_index.html", context)

def add_author(request):
    Author.objects.create(
        first_name = request.POST['first_name_input'],
        last_name = request.POST['last_name_input'],
        notes = request.POST['notes_input'],
    )
    return redirect("/authors")

def author_view(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.exclude(authors=author.id)
    }
    return render(request, "author_view.html", context)

def add_book_to_author(request, author_id):
    author = Author.objects.get(id = author_id)
    author.books.add(Book.objects.get(id=request.POST['book_select']))
    return redirect(f"/authors/{author.id}")


# ---------------End Author Data----------------------------------