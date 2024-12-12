from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, list_books, add_book, delete_book, search_books

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', list_books, name='list_books'),
    path('add/', add_book, name='add_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
    path('search/', search_books, name='search_books'),

     path('api/', include(router.urls)),
]
