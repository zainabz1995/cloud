from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
# Create your views here.
from cloudBS.forms import SignUpForm
from cloudBS.models import City
from django.http import JsonResponse
from django.db.models import Sum


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def population_chart(request):
    labels = []
    data = []

    queryset = City.objects.values('country__name').annotate(country_population=Sum('population')).order_by(
        '-country_population')
    for entry in queryset:
        labels.append(entry['country__name'])
        data.append(entry['country_population'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })