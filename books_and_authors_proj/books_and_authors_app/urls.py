from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("add_book", views.add_book),
    path("books/<int:book_id>", views.view_book),
    path("add_author_to_book/<int:book_id>", views.add_author_to_book),

    path("authors", views.author_index),
    path("add_author", views.add_author),
    path("authors/<int:author_id>", views.author_view),
    path("authors/add_book_to_author/<int:author_id>", views.add_book_to_author)
]