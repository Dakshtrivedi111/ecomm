from django.shortcuts import render
from products.models import Product 

def get_product(request, slug):

    try:
        product = Product.objects.get(slug =slug)

        context = {'product' : product}
        print("rr")

        #if request.GET['size']: ----- this line is not working underlined cmd is working, need to find why
        if request.GET.get('size'):
            size = request.GET('size')
            """price = product.get_product_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price"""
            print("dffd")
            print(size)
            #print(size)

        return render(request  , 'product/product.html' , context = context)

    except Exception as e:
        print(e)

"""def get_product_by_size(request, size):
    try:
        product = Product.objects.get(size = size)

        return render(request, 'product/product_size.html')
    except Exception as e:
        print(e)"""

