from django.urls import path
from .views import chart_select_view, add_purchase_view, sales_dist_view, add_product_view


app_name = 'products'

urlpatterns = [
    path('', chart_select_view, name='main-product-view'),
    path('add/', add_purchase_view, name='add-purchase-view'),
    #
    path('add_product/', add_product_view, name='add-product-view'),
    path('sales/', sales_dist_view, name='sale-view')
]