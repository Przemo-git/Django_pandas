from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Purchase

import pandas as pd
#Create your views here.
from products.models import Product
from .utils import get_simple_plot, get_salesman_from_id, get_image
from .forms import PurchaseForm, ProductForm
import matplotlib.pyplot as plt
import seaborn as sns
from django.contrib.auth.decorators import login_required
#
#
@login_required
#chronię ten widok za pomocą dekoratora
def sales_dist_view(request):
    error_message = ''
    try:
        df = pd.DataFrame(Purchase.objects.all().values())
        df['salesman_id'] = df['salesman_id'].apply(get_salesman_from_id)
        df.rename({'salesman_id': 'salesman'}, axis=1, inplace=True)
        df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        print(df)


        #kolejność
        plt.switch_backend('Agg')
        #plt.figure(figsize=(10,5))
        plt.xticks(rotation=45)
        sns.barplot(x='date', y='total_price',hue='salesman', data=df)
        plt.tight_layout()
        graph = get_image()

        return render(request, 'products/sales.html', {
            'graph': graph,
            'error_message': error_message
        })

    except:
        graph = None
        error_message = 'No database'
        return render(request, 'products/sales.html', {
            'graph': graph,
            'error_message': error_message
        })

@login_required
def chart_select_view(request):
    error_message = None
    df = None
    graph = None
    price = None
    try:
        product_df = pd.DataFrame(Product.objects.all().values())
        purchase_df = pd.DataFrame(Purchase.objects.all().values())
        product_df['product_id'] = product_df['id']
        # df = pd.merge(purchase_df, product_df, on='product_id')
        #print(purchase_df.shape)



        if purchase_df.shape[0] > 0:
            #merge, kolejność!
            df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y', 'date_y'], axis=1).rename({'id_x':'id','date_x':'date'},axis=1)
            print(df)
            price = df['price']
            if request.method == 'POST':
                print(request.POST)
                chart_type = request.POST['sales']   #
                date_from = request.POST['date_from']
                date_to = request.POST['date_to']

                df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
                print(df['date'])
                df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')    ###
                print(df2)
                print('chart_type',chart_type)
                print(date_from, date_to)
                if chart_type !='':
                    if date_from != '' and date_to != '':
                        df = df[(df['date'] >= date_from) & (df['date'] <= date_to)]   ###
                        df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                    graph = get_simple_plot(chart_type, x=df2['date'], y=df2['total_price'], data=df)
                else:
                    error_message = 'Please select a chart type to continue'
        else:
            error_message = 'No records in database'
    except:
        product_df = None
        purchase_df = None
        error_message = 'No records in database'

    return render(request, 'products/main.html', {
        'error_message': error_message,
        'graph': graph,
        'price': price
    })




@login_required
def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message = None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.salesman = request.user
        obj.save()

        form = PurchaseForm()
        added_message = 'The purchase has been added'
    return render(request, 'products/add.html',{
        'form': form,
        'added_message': added_message
    })
    #żeby zobaczyć pamiętaj wpisz ..performance/add


#####################################################################

@login_required
def add_product_view(request):
    form = ProductForm(request.POST or None)
    added_message = None

    if form.is_valid():

        obj = form.save()
        obj.save()

        form = ProductForm()
        added_message = 'The product has been added'
    return render(request, 'products/add_product.html', {
        'form': form,
        'added_message': added_message
    })




