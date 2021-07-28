from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from . models import TimeTable, Product, Day

# Create your views here.


def view_timetable(request):
    """ A view to renders the timetable page """

    timetable = TimeTable.objects.all()
    monday = TimeTable.objects.filter(day__day="Mon")
    tuesday = TimeTable.objects.filter(day__day="Tue")
    wednesday = TimeTable.objects.filter(day__day="Wed")
    thursday = TimeTable.objects.filter(day__day="Thu")
    friday = TimeTable.objects.filter(day__day="Fri")
    saturday = TimeTable.objects.filter(day__day="Sat")
    sunday = TimeTable.objects.filter(day__day="Sun")

    context = {
        'timetable': timetable,
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,
    }
    
    return render(request, 'timetable/timetable.html', context)
