from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Product, Wishlist
from .forms import FarmerRegistrationForm

def home(request):
    return render(request, 'index.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

def wishlist(request):
    return render(request, 'wishlist.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def about(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')

def my_account(request):
    return render(request, 'my-account.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = FarmerRegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def farmer_dashboard(request):
    return render(request, 'farmer_dashboard.html')

@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            return redirect('shop')
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    Wishlist.objects.create(product=product, user=request.user)
    return redirect('wishlist')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def inde_page(request):
    return render(request, 'inde.html')