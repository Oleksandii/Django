from django.shortcuts import render
from orders.models import SalesOrder
from rest_framework.viewsets import ModelViewSet



def orders_page(requsest):
    return render(requsest, 'index.html', {'orders': SalesOrder.objects.all()} )

class OrderViev(ModelViewSet):
    queryset = SalesOrder.objects.all()
    


# Create your views here.
