from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from . models import TimeTable, TimeTableItems, Product

# Create your views here.


def view_timetable(request):
    """ A view to renders the timetable page """

    timetables = TimeTableItems.objects.all()

    context = {
        'timetables': timetables,
    }

    return render(request, 'timetable/timetable.html', context)
