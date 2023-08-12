import base64
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
import seaborn as sns

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def one_bar_chart(x, y):
    plt.switch_backend("AGG")
    plt.figure(figsize = (12, 5))
    plt.bar(x, y)
    plt.tight_layout()
    graph = get_graph()
    return graph

def two_bar_chart(x, y, z):
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

def horizontal_barchart(x, y, z):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 5))
    y_axis = np.arange(len(y))
    plt.barh(y_axis - 0.2, x, 0.4, label='Golovi')
    plt.barh(y_axis + 0.2, z, 0.4, label='Asistencije')
    plt.yticks(y_axis, y)
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph

def performance_check(x, y, z, name):
    plt.switch_backend("AGG")
    plt.figure(figsize = (10, 5))
    plt.plot(x, y, label=name)
    plt.plot(x, z, label="Prosjek")
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_pie_chart(x, labels):
    plt.switch_backend("AGG")
    plt.pie(x, labels=["" for i in range(len(labels))], autopct='%.1f%%')
    plt.legend(labels, loc='upper right')
    plt.tight_layout()
    graph = get_graph()
    return graph

def positions_per_club(data):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 10))
    sns.catplot(hue = 'Pozicija', y = 'Klub',kind = 'count', data = data, legend_out=False)
    plt.legend(loc='lower right')
    plt.xlabel("Broj igrača")
    plt.tight_layout()
    graph = get_graph()
    return graph

def players_per_club(x, y):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=x, y=y,color="dodgerblue")
    plt.xticks(rotation=90)
    plt.xlabel(None)
    plt.tight_layout()
    graph = get_graph()
    return graph
