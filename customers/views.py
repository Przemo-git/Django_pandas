from django.shortcuts import render

# Create your views here.
import pandas as pd

from products.utils import get_image
from .models import Customer
import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.auth.decorators import login_required

@login_required
def customer_corr_view(request):
    error_message = None
    graph = None
    corr = ''
    try:
        df = pd.DataFrame(Customer.objects.all().values())
        corr = round(df['budget'].corr(df['employment']), 2)


        plt.switch_backend('Agg')
        sns.jointplot(x='budget', y='employment', kind='reg', data=df).set_axis_labels('Company_budget', 'No of employees')
        graph = get_image()

        return render(request, 'customers/main.html', {
            'graph': graph,
            'corr': corr,
            'error_message': error_message
        })

    except:
        error_message = 'No data'


        return render(request, 'customers/main.html', {
            'graph': graph,
            'corr': corr,
            'error_message': error_message
        })