from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import CsvForm
import csv
from .models import Csv
from products.models import Product, Purchase
from django.contrib.auth.decorators import login_required
#Create your views here.

... # mój dopis do oryginału

#do wczytania pierwszego pliku do bazy z csv trzeba ustawić usera jakiegoś!!!!!!!!!!!!!!!!!!!!!
@login_required
def upload_file_view(request):
    error_message = None
    success_message = None
    form = CsvForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            #
            if obj.activated == False:
                obj.delete()
            #
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for row in reader:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    print(row)
                    print(type(row))
                    user = User.objects.get(id=row[3])             #### get nie create bo już jest
                    prod ,_ = Product.objects.get_or_create(name=row[0])
                    #get_or_create unikamy duplikatów
                    Purchase.objects.create(                     ######################
                        product=prod,
                        price = int(row[2]),
                        quantity = int(row[1]),
                        salesman = user,
                        date = row[4] + " " + row[5]
                    )

            # kolejność!!!
            obj.activated = True
            obj.save()
            success_message = 'Uploaded succesfully'

        except:
            error_message = 'Ups..something went wrong, check data csv and try activate csv'


    return render(request, 'csvs/upload.html',{
        'form': form,
        'success_message': success_message,
        'error_message': error_message
    })


