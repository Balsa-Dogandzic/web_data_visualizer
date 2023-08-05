from django.shortcuts import render, HttpResponse
from .utils import get_barplot, get_pieplot
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
    df = pd.read_csv("static/cl_goals.csv")
    clubs = df[['Klub', 'Golovi']].groupby(by='Klub').sum()

    best_club = clubs[clubs['Golovi'] == clubs['Golovi'].max()]

    graph = get_pieplot(clubs.head(10)['Golovi'], clubs.head(10).index)

    return render(request, 'clubs.html', {'clubs':clubs, 'best_club':best_club, 'graph':graph})

def club(request, club):
    return render(request, 'club.html', {'club':club})

def players(request):
    return render(request, 'players.html')

def player(request, player):
    return render(request, 'player.html', {'player':player})
