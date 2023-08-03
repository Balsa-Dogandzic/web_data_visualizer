from django.shortcuts import render, HttpResponse
from .utils import get_barplot
import pandas as pd

# Create your views here.

def index(request):
    df = pd.read_csv("static/cl_goals.csv")
    df = df.sort_values(by='Golovi', ascending=False)

    x = df.head(10)['Igrač']
    y = df.head(10)['Golovi']
    chart = get_barplot(x, y)

    clubs = df['Klub'].unique()

    return render(request, 'index.html', {'chart':chart, 'clubs':clubs})

def clubs(request):
    return render(request, 'clubs.html')

def club(request, club):
    return render(request, 'club.html', {'club':club})
