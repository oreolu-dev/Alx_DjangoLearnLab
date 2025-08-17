# CRUD Operations

## Create

from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book, book.id

# Expected output:
# (<Book: 1984 by George Orwell (1949)>, 1)

---

## Retrieve

book = Book.objects.get(id=1)
book.title, book.author, book.publication_year

# Expected output:
# ('1984', 'George Orwell', 1949)

---

## Update

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

book.title

# Expected output:
# 'Nineteen Eighty-Four'

---

## Delete

book = Book.objects.get(id=1)
book.delete()

Book.objects.all()
# Expected output:
# <QuerySet []>

