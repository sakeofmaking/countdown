# countdown/views.py
from django.shortcuts import render
from countdown.models import Counter
from . import countdown as cd


def countdown_index(request):
    counters = Counter.objects.all()

    count_tos = []
    for counter in counters:
        count_tos.append(cd.date_to_sec(str(counter.count_to)))

    context = {
        'counters': counters,
        'count_tos': count_tos,
    }
    return render(request, 'countdown_index.html', context)
