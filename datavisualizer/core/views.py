from django.shortcuts import render, HttpResponse
from .utils import get_plot
import pandas as pd

# Create your views here.

def index(request):
    df = pd.read_csv("static/goals.csv")
    x = df.head(10)['player_name']
    y = df.head(10)['goals']
    chart = get_plot(x, y)
    return render(request, 'index.html', {'chart':chart})
