from django.shortcuts import render
from users.models import Profile

def index(request):
    labels = []
    data = []

    queryset = Profile.objects.order_by('-stress_level')[:5]
    for person in queryset:
        labels.append(person.user)
        data.append(person.stress_level)
    return render(request, 'greeting.html', {
        'labels': labels,
        'data': data
    })

