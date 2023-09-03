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
    plt.grid(True, alpha=0.5, zorder=0)
    plt.bar(x, y, zorder=3, color='#008b8b', edgecolor='#004646', linewidth=2)
    plt.xticks(fontsize='13', fontfamily='calibri')
    plt.yticks(fontsize='13', fontfamily='calibri')
    plt.tight_layout()
    graph = get_graph()
    return graph

def two_bar_chart(x, y, z):
    plt.switch_backend("AGG")
    plt.figure(figsize = (12, 5))
    x_axis = np.arange(len(x))
    plt.grid(True, alpha=0.5, zorder=0)
    plt.bar(x_axis - 0.21, y, 0.4, label="Golovi", color='#008b8b', edgecolor='#004646', linewidth=2, zorder=3)
    plt.bar(x_axis + 0.21, z, 0.4, label="Asistencije", color='#8B0000', edgecolor='#470101', linewidth=2, zorder=3)
    plt.xticks(x_axis, x, fontsize='12', fontfamily='calibri')
    legend = plt.legend()
    legend_text = legend.get_texts()
    plt.setp(legend_text, fontname='Calibri', fontsize=14, fontweight='bold')
    plt.tight_layout()
    graph = get_graph()
    return graph

def horizontal_barchart(x, y, z):
    plt.switch_backend("AGG")
    plt.figure(figsize=(12, 6))
    y_axis = np.arange(len(y))
    plt.grid(True, alpha=0.5, zorder=0)
    plt.barh(y_axis - 0.22, x, 0.4, label='Golovi', color='#008b8b', edgecolor='#004646', linewidth=2, zorder=3)
    plt.barh(y_axis + 0.22, z, 0.4, label='Asistencije', color='#8B0000', edgecolor='#470101', linewidth=2, zorder=3)
    plt.yticks(y_axis, y, fontsize='13', fontfamily='calibri')
    plt.xticks(fontsize='12', fontfamily='calibri')
    legend = plt.legend()
    legend_text = legend.get_texts()
    plt.setp(legend_text, fontname='Calibri', fontsize=14, fontweight='bold')
    plt.tight_layout()
    graph = get_graph()
    return graph

def performance_check(x, y, z, name):
    plt.switch_backend("AGG")
    plt.figure(figsize = (12, 6))
    plt.plot(x, y, label=name)
    plt.plot(x, z, label="Prosjek")
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph

def pie_chart(x, labels):
    plt.switch_backend("AGG")
    plt.pie(x, labels=["" for i in range(len(labels))], autopct='%.1f%%')
    plt.legend(labels, loc='upper right')
    plt.tight_layout()
    graph = get_graph()
    return graph

def positions_per_club(data):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 10))
    sns.catplot(hue = 'Pozicija', y = 'Klub', kind='count', data = data, legend_out=False)
    plt.legend(loc='lower right')
    plt.xlabel("Broj igrača")
    plt.ylabel(None)
    plt.tight_layout()
    graph = get_graph()
    return graph

def players_per_club(x, y):
    plt.switch_backend("AGG")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=x, y=y, color='#008b8b')
    sns.set_style('whitegrid')
    plt.xticks(rotation=90, fontsize='12', fontfamily='calibri')
    plt.yticks(fontsize='12', fontfamily='calibri')
    plt.xlabel(None)
    plt.tight_layout()
    graph = get_graph()
    return graph
