from django.db.models import Count, OuterRef, Subquery
from django.shortcuts import render

from journal.models import DailyEntry


def index(request):
    last_level_sq = (
        DailyEntry.objects
        .filter(user=OuterRef('user'))
        .order_by('-created_at')
        .values('stress_level')[:1]
    )

    per_user = (
        DailyEntry.objects
        .values('user')
        .annotate(stress_level=Subquery(last_level_sq))
    )

    agg = (
        per_user
        .values('stress_level')
        .annotate(cnt=Count('user'))
        .order_by('stress_level')
    )

    counts = {i: 0 for i in range(11)}
    for row in agg:
        lvl = row['stress_level']
        if lvl is not None and 0 <= lvl <= 10:
            counts[lvl] = row['cnt']

    labels = [str(i) for i in range(11)]
    data = [counts[i] for i in range(11)]

    return render(request, 'greeting.html', {
        'labels': labels,
        'data': data
    })
