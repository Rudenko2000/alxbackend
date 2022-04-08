from django.shortcuts import render
from django.http import HttpRequest
import datetime

# Create your views here.

def home(request):
    now=datetime.datetime.now()
    godzina_otwarcia_strony=f"{now.hour}:{now.minute}:{now.second}"
    context = {'title': f"Pierwsza strona,",
               'title2': f" user agent: {request.headers['User-Agent']}",
               'title3': f" godzina otwarcia strony {godzina_otwarcia_strony}",
               'dump': request}

    return render(request, 'library/index.html', context)
