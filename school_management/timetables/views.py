from django.shortcuts import render, get_object_or_404, redirect
from .models import Timetable
from .form import TimetableForm

def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'timetable_list.html', {'timetables': timetables})

def timetable_create(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'timetable_form.html', {'form': form})