from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product, Wishlist
from .forms import FarmerRegistrationForm, ProductForm, BookingForm
from .models import Product, Wishlist

def home(request):
    return render(request, 'inde.html')

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
    if request.method == "POST":
        name = request.POST.get("name")
        user_email = request.POST.get("email")
        message_text = request.POST.get("message")
        
        subject = f"New message from {name}"
        message_body = f"From: {name} <{user_email}>\n\n{message_text}"
        
        send_mail(
            subject,
            message_body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        
        # Using the PRG pattern: redirect to the same page with a GET parameter
        return redirect('.')
    
    # Check for the success message in GET params
    message_sent = request.GET.get('message_sent')
    return render(request, 'inde.html', {'message_sent': message_sent})

def about(request):
    return render(request, 'about.html')

@login_required
def gallery(request):
    # Order by descending id (newest first)
    products = Product.objects.all().order_by('-id')
    # If you want to include an upload form in gallery, you can also pass a new form instance.
    form = ProductForm()
    return render(request, 'gallery.html', {'form': form, 'products': products})

def my_account(request):
    return render(request, 'my-account.html')

def shop_detail(request):
    # Example: get all products (each product was uploaded by a farmer)
    farmer_products = Product.objects.all()
    return render(request, 'shop-detail.html', {'farmer_products': farmer_products})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('farmer_dashboard')  # redirect to dashboard instead of home
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
    if request.method == "POST" and 'product_id' in request.POST:
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        # Update product fields
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.deposit_percentage = request.POST.get('deposit_percentage')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return redirect('farmer_dashboard')
        
    # Existing code to handle adding new products and fetching products for display
    products = Product.objects.filter(farmer=request.user)
    return render(request, 'farmer_dashboard.html', {'products': products})

@login_required
def upload_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = request.user
            product.save()
            # Redirect to gallery view after saving so that new product appears on top
            return redirect('gallery')
    else:
        form = ProductForm()
    # If GET or invalid POST, optionally re-render dashboard form with errors.
    products = Product.objects.filter(farmer=request.user)
    return render(request, 'farmer_dashboard.html', {'form': form, 'products': products})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    # Removed 'user=request.user' since the Wishlist model does not have a 'user' field
    Wishlist.objects.create(product=product)
    return redirect('wishlist')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def inde_page(request):
    return render(request, 'inde.html')

def book_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    total_booked = sum(booking.quantity for booking in product.bookings.all())
    remaining_stock = product.stock - total_booked

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_quantity = form.cleaned_data['quantity']
            if booking_quantity > remaining_stock:
                form.add_error('quantity', f'Only {remaining_stock} remaining for booking.')
            else:
                booking = form.save(commit=False)
                booking.product = product
                booking.save()
                 
                # Include farmer details for internal notification only
                farmer = product.farmer
                farmer_details = (
                    f"Farmer Name: {farmer.name}\n"
                    f"Farmer Email: {farmer.email}\n"
                    f"Farmer Phone: {farmer.phone_number}\n"
                    f"Farmer Location: {farmer.location}\n"
                )
                
                subject = f"New Booking for {product.name}"
                message = (
                    f"Booking Details:\n\n"
                    f"Product: {product.name}\n"
                    f"Customer Name: {booking.customer_name}\n"
                    f"Location: {booking.location}\n"
                    f"Phone: {booking.phone_number}\n"
                    f"Email: {booking.email}\n"
                    f"Quantity Booked: {booking.quantity}\n\n"
                    f"Farmer Details (Internal Use):\n{farmer_details}"
                )
                # Email will be sent internally; the customer never sees these details
                recipient = [settings.EMAIL_HOST_USER]
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient, fail_silently=False)
                
                # Optionally, send a customer confirmation message not including farmer details
                
                return redirect('booking_confirm')
    else:
        form = BookingForm()
    return render(request, 'Booking_Template.html', {'product': product, 'form': form, 'remaining_stock': remaining_stock})

def booking_confirm(request):
    return render(request, 'booking_confirm.html')

@csrf_exempt
def update_like(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        # Increment like count in database for the post here.
        # For now, return a dummy value.
        new_like_count = 1  # Replace with actual incremented value
        return JsonResponse({'likes': new_like_count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def update_view(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        # Increment view count and return new count.
        new_view_count = 1  # Replace with actual value
        return JsonResponse({'views': new_view_count})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def submit_comment(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        comment_text = request.POST.get('comment')
        # Simulate saving the comment and updating the comment count.
        # In a real view, you'd update your database here.
        comments_html = "<p>" + comment_text + "</p>"  # Dummy comment HTML
        new_count = 1  # Dummy count (replace with your updated count)
        return JsonResponse({'comments_html': comments_html, 'count': new_count})
    return JsonResponse({'error': 'Invalid request'}, status=400)