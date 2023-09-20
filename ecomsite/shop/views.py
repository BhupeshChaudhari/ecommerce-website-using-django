from django.shortcuts import render
from .models import Products, Orders
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    product_objects = Products.objects.all()

    #search code --> Always above the Paginator code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains = item_name)
  
    #Paginator code
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    context = {
        'product_objects' : product_objects,
    }

    return render(request, 'shop/index.html' , context)

def detail(request, id):
    product_object = Products.objects.get(id=id)
    context = {
        'product_object' : product_object,
    }

    return render(request, 'shop/detail.html', context)

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip',"")
        total = request.POST.get('total', "")

        order = Orders(items=items, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)   
        order.save()

    return render(request, 'shop/checkout.html')