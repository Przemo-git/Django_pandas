import base64
from io import BytesIO

import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.auth.models import User


def get_salesman_from_id(val):
    salesman = User.objects.get(id=val)
    return salesman

def get_image():
    buffer = BytesIO()  ##
    plt.savefig(buffer, format='png')
    #set cursor to beginning
    buffer.seek(0)
    image_png = buffer.getvalue()   ###

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    buffer.close()
    return graph


def get_simple_plot(chart_type, *args, **kwargs):
    #https://matplotlib.org/2.0.2/faq/usage_faq.html#what-is-a-backend
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,7))    ####
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    if chart_type == 'bar plot':     ###
        #muszą być małe litery
        #uwaga formularz menu muszą być b. precyzyjne nazwy
        title = 'total price by day (bar)'
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line plot':
        title = 'total price by day (line)'
        plt.title(title)
        plt.plot(x, y)
    else:
        title = 'product count'
        plt.title(title)
        sns.countplot('name', data=data)
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = get_image()
    return graph


