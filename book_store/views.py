from django.http import HttpResponse
from .models import Book


# Create your views here.


def index(request):
    books = Book.objects.all()
    """ for b in books:
        print(b) """
    print(books.count())

    return HttpResponse("Welcome to my book store.")
