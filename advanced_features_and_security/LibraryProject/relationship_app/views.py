"""
Permissions and Groups Setup:
- Custom permissions added in Book model (can_view, can_create, can_edit, can_delete).
- Groups to configure in Admin:
    * Viewers → can_view
    * Editors → can_create, can_edit
    * Admins → all permissions
- Views are protected with @permission_required decorators.
"""


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View books (anyone with can_view)
@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})

# Create book
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        Book.objects.create(title=title, author=author, publication_year=year)
        return redirect('view_books')
    return render(request, 'relationship_app/add_book.html')

# Edit book
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('year')
        book.save()
        return redirect('view_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# Delete book
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('view_books')
