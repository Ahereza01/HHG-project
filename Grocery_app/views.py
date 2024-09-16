from django.shortcuts import render, redirect
#accessing the models so that we can interact with the database
from Grocery_app.models import Stockx
#borrowing decorators from django to restrict access to our pages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.views import LogoutView
from .filters import StockxFilter


# Create your views here.
def index(request):
    return render(request, 'Grocery_app/access.html')

def register(request):
    return render(request, 'Grocery_app/register.html')


@login_required
def home(request):
    products = Stockx.objects.all().order_by('-id')
    product_filters = StockxFilter(request.GET, queryset = products)
    products = product_filters.qs
    return render(request, 'Grocery_app/home.html',{'products': products, 'product_filters': product_filters})

@login_required
def product_detail(request, product_id):
    product = Stockx.objects.get(id=product_id)
    return render(request, 'Grocery_app/product_detail.html', {'product': product})

@login_required
def delete_detail(request, product_id):
    product = Stockx.objects.get(id=product_id)
    product.delete()
    return redirect('home')

@login_required
def issue_item(request,pk):
    #accessing all objects from the Stockx model
    issued_item = Stockx.objects.get(id=pk)
    #accessing the form for editing the object
    sales_form = SaleForm(request.POST)
    #receiving data from the form and saving it to the model/database
    if request.method == 'POST':
    #checking if the form is valid
       if sales_form.is_valid():
           new_sale = sales_form.save(commit=False)
           new_sale.item = issued_item
           new_sale.unit_price = issued_item.unit_price
           new_sale.save()
           #keep track of the remaining stock after sales
           issued_quantinty = int(request.POST['quantity'])
           issued_item.total_quantity -= issued_quantinty
           issued_item.save()




           return redirect('receipt')
    return render(request, 'Grocery_app/issue_item.html', {'sales_form': sales_form})

@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request, 'Grocery_app/receipt.html', {'sales': sales})


@login_required
def receipt_detail(request, receipt_id):
    receipt = Sale.objects.get(id=receipt_id)
    return render(request, 'Grocery_app/receipt_detail.html', {'receipt': receipt})


def index(request):
    products = Stockx.objects.all().order_by('-id')
    return render(request,"Grocery_app/index.html", {'products': products})
@login_required
def log_out(request):
    logout(request)
    return redirect('index')

@login_required
def all_sales(request):
    sales = Sale.objects.all().order_by('-id')
    total_expected = sum([items.get_total() or 0  for items in sales])
    total = sum([items.amount_received or 0 for items in sales])
    total_change = sum([items.get_change() or 0  for items in sales])
    net = total_expected - total
    return render(request, 'Grocery_app/all_sales.html', {'sales': sales, 'total':total, 'total_change':total_change, 'net':net, 'total_expected':total_expected})

@login_required
def add_stock(request, pk):
    #calling for each object with its id
    issued_item = Stockx.objects.get(id=pk) 
    form = AddForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
             #filering the value from the form and adding it to the form fields 
            added_quantity = int(request.POST['total_quantity'])
             #to add to the remaining stock, quantity is increasing
            issued_item.total_quantity += added_quantity
            issued_item.save()
            print(added_quantity)
            print(issued_item.total_quantity)
            return redirect('home')
        
    return render(request, 'Grocery_app/add_stock.html', {'form': form})
        









    




   
   
    
