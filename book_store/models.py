from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)


""" # Retrieving all books
books = Book.objects.all()
print(books)
# Filtering books by author
books_by_author = Book.objects.filter(author="John Doe")

# Ordering books by published date
books_ordered = Book.objects.order_by("published_date")

# Creating a new book
new_book = Book(title="New Book", author="Jane Smith", published_date="2023-01-01")
# new_book.save() """
