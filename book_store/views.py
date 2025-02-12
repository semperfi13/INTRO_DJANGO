from django.http import HttpResponse
from .models import Product


# Create your views here.


def index(request):
    product = Product.objects.create(
        name="APPLE",
        description="From NIGER",
        price=500,
        category="FRUITS",
    )
    product.save()
    products = Product.objects.filter(category="FRUITS").order_by("id")

    for p in products:
        print(
            f"{p.id} \n{p.name} from {p.description}, category: {p.category}, is {p.price}$"
        )

    return HttpResponse("Welcome to my book store.")
