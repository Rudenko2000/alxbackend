import datetime

from django.shortcuts import render
from django.http import HttpRequest

from .models import Book, Author



# Create your views here.

def home(request):

    now=datetime.datetime.now()
    books=Book.objects.all()
    godzina_otwarcia_strony=f"godzina: {now.hour}, minuta: {now.minute}, sekunda: {now.second}."
    przegladarka=request.headers['User-Agent']
    time=datetime.datetime.now().strftime("%H:%M:%S")



    context = {'title': f"django ALX backend,",
               'title1': f"Pierwsza strona",
               'title2': f" Przeglądarka: {przegladarka}",
               'title3': f" godzina otwarcia strony: {godzina_otwarcia_strony}, czyli: {time}",
               "books":books,
               }

    return render(request, 'library/index.html', context)

def book(request,book_id):
   book=Book.objects.get(id=book_id)
   return render(request, "library/book.html",{"book":book})

def author(request,author_id):

   author=Author.objects.get(id=author_id)
   listabooks = author.book_set.all()
   return render(request, "library/author.html",{"author":author, "listabooks": listabooks})


