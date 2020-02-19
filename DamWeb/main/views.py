from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'Author': 'Ekansh',
        'Title': 'Pressure Meter',
        'Content': '102002 psi',
        'data': 'Feb 19 2020',
    },
    {
        'Author':'Ekansh1',
        'Title':'Pressure1 Meter',
        'Content':'1020021 psi',
        'data':'Feb 19 20120',
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'main/main.html',context)


def about(request):
    return render(request, 'main/about.html')
