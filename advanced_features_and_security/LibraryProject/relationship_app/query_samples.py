import os
import django

# -----------------------------
# Setup Django environment
# -----------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author.name}:")
    for book in books:
        print(f"- {book.title}")


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library.name} Library:")
    for book in books:
        print(f"- {book.title}")


# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"The librarian of {library.name} Library is {librarian.name}")


if __name__ == "__main__":
    # Replace these with actual data from your database
    books_by_author("Chimamanda Ngozi Adichie")
    books_in_library("President Obasanjo Library")
    librarian_of_library("President Obasanjo Library")
