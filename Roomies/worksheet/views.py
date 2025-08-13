from django.shortcuts import render
from .models import User, Task

def timetable_view(request):
    days = ['Monday', 'Tuesday', 'Wednesday','Thuesday','Friday','Saturaday','Sunday']
    user = User.objects.all()
    timetable = {}

    for user in user:
        timetable[user] = {}
        for day in days:
            tasks = Task.objects.filter(user=user, day=day)
            timetable[user][day] = ", ".join(t.task for t in tasks)

    return render(request, 'worksheet/timetable.html', {'timetable': timetable, 'days': days})