from django.shortcuts import render, redirect
from django.contrib import messages
from market.models import *
from django.contrib.auth.decorators import login_required
import random
from django.http.response import  JsonResponse




def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders':orders
    }
    return render(request, 'market/orders/index.html', context)

def vieworder(request, t_no):
    order = Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
    context = {
        'order':order,
        'orderitems':orderitems
    }
    return render(request, 'market/orders/vieworder.html ', context)