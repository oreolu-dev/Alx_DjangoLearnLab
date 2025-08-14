## command
from bookshelf.models import Book
from django.forms.models import model_to_dict

book = Book.objects.get(title=1984, author=George Orwell, publication_ye
ar=1949)
model_to_dict(book)

## Expected output
## {'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}
