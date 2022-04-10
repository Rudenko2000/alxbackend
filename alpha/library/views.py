import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import Book, Author
from .forms import AddBookForm, BookForm_ModelForm, DeleteBookForm


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


def book(request, book_id):
    # book = Book.objects.get(id=book_id)
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = DeleteBookForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["operation"] == "delete":
                book.delete()
                messages.success(request, "Usunięto książkę")
                return HttpResponseRedirect(reverse("home"))
    delete_form = DeleteBookForm()
    return render(request, 'library/book.html', {'book': book, "delete_form": delete_form})


def author(request,author_id):

   author=Author.objects.get(id=author_id)
   listabooks = author.book_set.all()
   return render(request, "library/author.html",{"author":author, "listabooks": listabooks})


def add_book(request):
    if request.method=="POST":
       form=AddBookForm(request.POST)
       if form.is_valid():
          author=Author.objects.get(name=form.cleaned_data["author_name"])
          book=Book(title=form.cleaned_data["title"],
                    author=author,
                    description=form.cleaned_data["description"]
        )
          book.save()
          messages.add_message(request, messages.SUCCESS, "Dodano")
          messages.success(request, "Dodano jest")
          return HttpResponseRedirect(reverse('book', args=(book.id,)))
    else:
        form=AddBookForm
    return render(request, "library/add_book.html", {"form":form})

def add_book_modelform(request):
    form = BookForm_ModelForm()
    if request.method=="POST":
        form=BookForm_ModelForm(request.POST)
        if form.is_valid():
            book=form.save()
            messages.success(request, "Dodano jest")
            return HttpResponseRedirect(book.get_absolut_url())

    else:
        form = BookForm_ModelForm()

    return render(request, "library/add_book.html", {"form":form})