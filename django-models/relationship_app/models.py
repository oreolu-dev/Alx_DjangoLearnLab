from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    # Each book belongs to ONE author, but an author can write MANY books
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    # A library can contain MANY books, and a book can exist in MANY libraries
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # Each library has exactly ONE librarian (and each librarian belongs to ONE library)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




