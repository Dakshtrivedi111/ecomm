from django.urls import path
from products.views import *

urlpatterns = [
   
    path('<slug>/' , get_product , name="get_product")
    #path('<size>/',get_product_by_size, name = "get_product_by_size")
]