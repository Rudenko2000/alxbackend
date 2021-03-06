"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import library.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', library.views.home,name="home"),
    path('books/add', library.views.add_book, name='add book'),
    path('books/add_modelform', library.views.add_book_modelform, name='add book with modelform'),
    path("books/<int:book_id>",library.views.book, name = "book"),
    path("authors/<int:author_id>",library.views.author, name = "author"),

]
