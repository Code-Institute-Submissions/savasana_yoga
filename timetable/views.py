from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from products.models import Product

# Create your views here.

def view_timetable(request):
    """ A view to renders the timetable page """
    return render(request, 'timetable/timetable.html')
