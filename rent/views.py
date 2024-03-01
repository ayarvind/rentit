from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from .form import ProductForm
# Create your views here.
def add_product(request):
    productForm = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if not product_form.is_valid():
            return JsonResponse({
                'status': 'failed',
                'message': 'Invalid input'
            }, status=400)
        product_form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Product added successfully',
        }, status=201)
    else:
       return render(request, 'add_product.html', {'product_form': productForm})


    
    