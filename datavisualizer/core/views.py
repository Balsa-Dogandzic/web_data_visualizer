from django.shortcuts import render
from .utils import top10_players, top10_clubs, performance_check, get_pie_chart
import pandas as pd


def index(request):
    """Funkcija za pocetnu stranicu"""
    df = pd.read_csv("static/cl_goals.csv")
    df = df.sort_values(by='Golovi', ascending=False)

    x = df.head(10)['Igrač']
    y = df.head(10)['Golovi']
    chart = top10_players(x, y)

    clubs = df['Klub'].unique()

    return render(request, 'index.html', {
        'chart':chart,
        'clubs':clubs
    })


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

    return render(request, 'clubs.html', {
        'clubs':clubs, 
        'best_club':best_club, 
        'graph':graph
    })


def club(request, club):
    """Funkcija za stranicu o pojedinacnom klubu"""
    df = pd.read_csv("static/cl_goals.csv")
    all_clubs = df.groupby(["Klub"]).sum()

    try:
        club_data = all_clubs.loc[club]
    except:
        return render(request, "error_pages/404.html")
    clubs_mean = all_clubs[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()
    players = df[df["Klub"] == club]

    x = ['Broj mečeva', 'Golovi', 'Asistencije', 'Broj faulova', 'Šutevi']
    y = club_data[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']]
    z = clubs_mean
    graph = performance_check(x, y, z, club)

    return render(request, 'club.html', {
        'club':club_data, 
        'players':players, 
        "graph":graph
    })


def players(request):
    """Funkcija za stranicu o igracima"""
    df = pd.read_csv("static/cl_goals.csv")
    df = df.sort_values(by='Golovi', ascending=False)

    x = df.head(10)['Igrač']
    y = df.head(10)['Golovi']
    top10_graph = top10_players(x, y)

    position_counts = df.value_counts("Pozicija")
    positions_graph = get_pie_chart(position_counts, position_counts.index)

    return render(request, 'players.html', {
        "top10_graph":top10_graph, 
        'positions_graph':positions_graph
    })


def player(request, player):
    """Funkcija za stranicu o pojedinacnom igracu"""
    df = pd.read_csv("static/cl_goals.csv")

    player_data = df.loc[df['Igrač'] == player]
    if player_data.empty:
        return render(request, "error_pages/404.html")
    players_mean = df[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()

    x = players_mean.index
    y = player_data[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].values[0]
    z = players_mean
    performance_graph = performance_check(x, y, z, player)

    x = player_data[['Golovi_desnom', 'Golovi_lijevom', 'Golovi_glavom', 'Drugačiji_golovi']]
    goal_type_chart = get_pie_chart(x.values[0], x.columns)

    x = player_data[['Iz_šesnaesterca', 'Van_šesnaesterca']]
    goal_distance_chart = get_pie_chart(x.values[0], x.columns)

    return render(request, 'player.html', {
        'player_name':player,
        'player':player_data, 
        'performance_graph':performance_graph,
        'goal_type_chart':goal_type_chart,
        'goal_distance_chart':goal_distance_chart
    })
