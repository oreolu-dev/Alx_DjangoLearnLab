## command
from bookshelf.models import Book

book = Book.objects.get(title=Nineteen Eighty-Four, author=George Orwell, publication_year=1949)
book.delete()

## Expected output
## (1, {'bookshelf.Book': 1})

## command
Book.objects.all()

## Expected output
## <QuerySet []>
