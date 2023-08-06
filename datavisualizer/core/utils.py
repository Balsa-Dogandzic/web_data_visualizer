import base64
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def top10_players(x, y):
    plt.switch_backend("AGG")
    plt.figure(figsize = (12, 5))
    plt.bar(x, y)
    plt.tight_layout()
    graph = get_graph()
    return graph

def top10_clubs(x, y, z):
    plt.switch_backend("AGG")
    plt.figure(figsize = (12, 5))
    x_axis = np.arange(len(x))
    plt.bar(x_axis - 0.2, y, 0.4, label="Golovi")
    plt.bar(x_axis + 0.2, z, 0.4, label="Asistencije")
    plt.xticks(x_axis, x)
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph

def club_performance(x, y, z, klub):
    plt.switch_backend("AGG")
    plt.figure(figsize = (10, 5))
    plt.plot(x, y, label=klub)
    plt.plot(x, z, label="Prosjek")
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph