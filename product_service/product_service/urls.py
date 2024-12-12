# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse
# from django.shortcuts import redirect
# from product.views import book_management  # Import book_management

# def home(request):
#     return HttpResponse("Welcome to the Product Service!")

# urlpatterns = [
#     path('', home, name='home'),
#     path('admin/', admin.site.urls),
#     path('api/', include('product.urls')),  
#     path('book-management/', book_management, name='book-management'),  # Add the book-management route
# ]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
]

