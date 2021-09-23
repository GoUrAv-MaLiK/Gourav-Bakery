from .models import Product
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login') 
def Product_display(request):
    products=Product.objects.all()
    length=len(products)
    context={'product' :products, 'range':range(3),'n':length}
    return render(request, 'customer/homepage.html',context)