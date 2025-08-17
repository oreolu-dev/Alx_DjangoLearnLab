from django.urls import path
from . import views

urlpatterns = [
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:pk>/', views.delete_book, name='delete_book'),
]
