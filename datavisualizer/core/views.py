from django.shortcuts import render
from .utils import (one_bar_chart, two_bar_chart, performance_check, pie_chart, 
                    positions_per_club, players_per_club, horizontal_barchart)
import pandas as pd


def index(request):
    """Funkcija za pocetnu stranicu"""
    df = pd.read_csv("static/cl_goals.csv")

    x = df.head(10)['Igrač']
    y = df.head(10)['Golovi']
    chart = one_bar_chart(x, y)

    clubs = df['Klub'].unique()

    return render(request, 'index.html', {
        'chart':chart,
        'clubs':clubs
    })


def clubs(request):
    """Funkcija za stranicu o klubovima"""
    df = pd.read_csv("static/cl_goals.csv")
    clubs = df[['Klub', 'Golovi', 'Asistencije','Broj_faulova','Šutevi']].groupby(by='Klub').sum()
    clubs = clubs.sort_values(by=["Golovi", "Asistencije"], ascending=[False, False])

    club_counts = df.value_counts("Klub")
    p_per_c_graph = players_per_club(club_counts.index, club_counts.values)

    best_club = clubs.iloc[0]

    x = clubs.head(10).index
    y = clubs.head(10)['Golovi']
    z = clubs.head(10)['Asistencije']

    top10_graph = two_bar_chart(x, y, z)

    return render(request, 'clubs.html', {
        'clubs':clubs, 
        'best_club':best_club, 
        'top10_graph':top10_graph,
        'players_per_club':p_per_c_graph
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

    df_mean = df[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()
    club_mean = players[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()
    y = club_mean
    z = df_mean
    graph2 = performance_check(x, y, z, club)

    x = players['Golovi']
    y = players['Igrač']
    z = players['Asistencije']
    best_club_players = horizontal_barchart(x, y, z)

    return render(request, 'club.html', {
        'club':club_data, 
        'players':players, 
        'graph':graph,
        'graph2':graph2,
        'best_club_players': best_club_players
    })


def players(request):
    """Funkcija za stranicu o igracima"""
    df = pd.read_csv("static/cl_goals.csv")

    best_player = df.iloc[0]

    x = df.head(10)['Igrač']
    y = df.head(10)['Golovi']
    z = df.head(10)['Asistencije']
    top10_graph = two_bar_chart(x, y, z)

    position_counts = df.value_counts("Pozicija")
    positions_graph = pie_chart(position_counts, position_counts.index)

    positions_p_club = positions_per_club(df)

    return render(request, 'players.html', {
        'best_player':best_player,
        'top10_graph':top10_graph, 
        'positions_graph':positions_graph,
        'positions_per_club': positions_p_club
    })


def player(request, player):
    """Funkcija za stranicu o pojedinacnom igracu"""
    df = pd.read_csv("static/cl_goals.csv")

    player_data = df.loc[df['Igrač'] == player]
    if player_data.empty:
        return render(request, "error_pages/404.html")
    players_mean = df[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].mean()

    x = ['Broj mečeva', 'Golovi', 'Asistencije', 'Broj faulova', 'Šutevi']
    y = player_data[['Broj_mečeva', 'Golovi', 'Asistencije', 'Broj_faulova', 'Šutevi']].values[0]
    z = players_mean
    performance_graph = performance_check(x, y, z, player)

    x = player_data[['Golovi_desnom', 'Golovi_lijevom', 'Golovi_glavom', 'Drugačiji_golovi']]
    labels = ['Golovi desnom', 'Golovi lijevom', 'Golovi glavom', 'Drugačiji golovi']
    goal_type_chart = pie_chart(x.values[0], labels)

    x = player_data[['Iz_šesnaesterca', 'Van_šesnaesterca']]
    labels = ['Iz šesnaesterca', 'Van šesnaesterca']
    goal_distance_chart = pie_chart(x.values[0], labels)

    return render(request, 'player.html', {
        'player_name':player,
        'player':player_data, 
        'performance_graph':performance_graph,
        'goal_type_chart':goal_type_chart,
        'goal_distance_chart':goal_distance_chart
    })
