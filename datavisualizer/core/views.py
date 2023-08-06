from django.shortcuts import render, HttpResponse
from .utils import top10_players, top10_clubs, club_performance
import pandas as pd

def index(request):
    """Funkcija za pocetnu stranicu"""
    df = pd.read_csv("static/cl_goals.csv")
    df = df.sort_values(by='Golovi', ascending=False)

    x = df.head(10)['Igrač']
    y = df.head(10)['Golovi']
    chart = top10_players(x, y)

    clubs = df['Klub'].unique()

    return render(request, 'index.html', {'chart':chart, 'clubs':clubs})

def clubs(request):
    """Funkcija za stranicu o klubovima"""
    df = pd.read_csv("static/cl_goals.csv")
    clubs = df[['Klub', 'Golovi', 'Asistencije']].groupby(by='Klub').sum()
    clubs = clubs.sort_values(by="Golovi", ascending=False)

    best_club = clubs.iloc[0]

    x = clubs.head(10).index
    y = clubs.head(10)['Golovi']
    z = clubs.head(10)['Asistencije']

    graph = top10_clubs(x, y, z)

    return render(request, 'clubs.html', {'clubs':clubs, 'best_club':best_club, 'graph':graph})

def club(request, club):
    """Funkcija za stranicu o pojedinacnom klubu"""
    df = pd.read_csv("static/cl_goals.csv")
    df_mean = df[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()
    players = df[df["Klub"] == club]
    club_mean = players[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()
    x = club_mean.index
    y = club_mean
    z = df_mean
    graph = club_performance(x, y, z, club)
    return render(request, 'club.html', {'club':club, 'players':players, "graph":graph})

def players(request):
    """Funkcija za stranicu o igracima"""
    return render(request, 'players.html')

def player(request, player):
    """Funkcija za stranicu o pojedinacnom igracu"""
    return render(request, 'player.html', {'player':player})
