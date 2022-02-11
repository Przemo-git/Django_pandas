from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import LoginForm

def home_view(request):
    return render(request, 'home.html',{})

def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        print(form.data)
        #dlatego przechwytujemy do form
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    #dlatego blokowaliśmy login w settings żeby wiedzieć co dać po poniższym returnie(z adresu url):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')
            else:
                error_message = 'Ups..Something went wrong'
    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def logout_view(request):
    logout(request)
    return render(request, 'home.html', {})


from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext

# Create your views here.


def home(request):
    transl = translate(language='pl')
    return render(request, 'login.html', {
        'transl': transl
    })




# def translate(language):
#     cur_language = get_language()
#     try:
#         activate(language)
#         text = gettext('hello')
#         #text2 = gettext('This page:  hello item page translated to polish')
#     finally:
#         activate(cur_language)
#     return text





def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        # text = gettext('login')
        # text2 = gettext('home')
        # text3 = gettext('performance')
        # text4 = gettext('sales')
        # text5 = gettext('customers')
        # text6 = gettext('all records')
        # text7 = gettext('add new product')
        # text7 = gettext('uploads')
        # text7 = gettext('choose a chart type')
        # text7 = gettext('Date from')
        # text8 = gettext('Date to')
        # text9 = gettext('See Summary')
        # text9 = gettext('select')
        # text10 = gettext('add records')
        # text11 = gettext('Bar plot')
        # text12 = gettext('line plot')
        # text13 = gettext('count plot')
        # text14 = gettext('total price by day(bar)')
        # text15 = gettext('customer data')
        # text16 = gettext('Correlation')
        # text17 = gettext('Add sale data')
        # text18 = gettext('Add product')
        # text18 = gettext('Price data')
        # text19 = gettext('Count')
        # text20 = gettext('Mean')
        # text21 = gettext('Median')
        # text22 = gettext('Std dev')
        # text33 = gettext('Sales')
        # text34 = gettext('Add sale data')
    finally:
        activate(cur_language)
    return




#https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#gettext-on-windows
#...binary installer
