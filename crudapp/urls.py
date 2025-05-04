from django.urls import path
from django.contrib.auth import views as auth_views 
from django.views.generic.base import RedirectView
from . import views
from crudapp import views as crud_views

urlpatterns = [

    path('', views.home, name='home'), 
    

    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('my-account/', views.my_account, name='my_account'),
    path('shop-detail/', views.shop_detail, name='shop_detail'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('upload-product/', views.upload_product, name='upload_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('register_farmer/', views.register_view, name='register_farmer'),
    path('farmer-dashboard/products/', views.product_list, name='product_list'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'
        ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ), name='password_reset_complete'),
    path('inde/', crud_views.inde_page, name='inde'),
    path('contact/', views.contact_us, name='contact'),
    path('index.html', views.home, name='home_index'),  # Optional: if you really need /index.html
    path('contact-us/index.html', RedirectView.as_view(url='/contact-us/', permanent=True)),
    path('about.html', RedirectView.as_view(url='/about/', permanent=True)),
    path('shop-detail.html', RedirectView.as_view(url='/shop-detail/', permanent=True)),
    path('contact-us/about.html', RedirectView.as_view(url='/about/', permanent=True)),
    path('contact-us/shop-detail.html', RedirectView.as_view(url='/shop-detail/', permanent=True)),
    path('contact-us/shop.html', RedirectView.as_view(url='/shop/', permanent=True)),
    path('contact-us/about.html', RedirectView.as_view(url='/about/', permanent=True)),
    path('contact-us/index.html', RedirectView.as_view(url='/', permanent=True)),
    path('contact-us/shop-detail.html', RedirectView.as_view(url='/shop-detail/', permanent=True)),
    path('shop/gallery.html', RedirectView.as_view(url='/gallery/', permanent=True)),
    path('gallery/contact-us.html', RedirectView.as_view(url='/contact-us/', permanent=True)),
    path('contact-us/gallery.html', RedirectView.as_view(url='/gallery/', permanent=True)),
    path('gallery/about.html', RedirectView.as_view(url='/about/', permanent=True)),
    path('gallery/index.html', RedirectView.as_view(url='/gallery/', permanent=True)),
    path('gallery/shop-detail.html', RedirectView.as_view(url='/shop-detail/', permanent=True)),
   path('gallery/gallery.html', RedirectView.as_view(url='/gallery/', permanent=True)),
path('shop/gallery.html', RedirectView.as_view(url='/gallery/', permanent=True)),
path('shop/shop-detail.html', RedirectView.as_view(url='/shop-detail/', permanent=True)),
path('shop/index.html', RedirectView.as_view(url='/shop/', permanent=True)),
path('shop/contact-us.html', RedirectView.as_view(url='/contact-us/', permanent=True)),
path('shop/about.html', RedirectView.as_view(url='/about/', permanent=True)),
path('contact-us/wishlist.html', RedirectView.as_view(url='/wishlist/', permanent=True)),
path('wishlist/gallery.html', RedirectView.as_view(url='/wishlist/', permanent=True)),
path('wishlist/index.html', RedirectView.as_view(url='/wishlist/', permanent=True)),
path('wishlist/shop-detail.html', RedirectView.as_view(url='/shop-detail/', permanent=True)),
path('wishlist/shop.html', RedirectView.as_view(url='/shop/', permanent=True)),
path('wishlist/about.html', RedirectView.as_view(url='/about/', permanent=True)),
path('wishlist/contact-us.html', RedirectView.as_view(url='/contact-us/', permanent=True)),
 path('book/<int:product_id>/', views.book_product, name='book_product'),
 path('booking-confirm/', views.booking_confirm, name='booking_confirm'),
 path('contact-us/', views.contact_us, name='contact_us'),

    path('contact-us/gallery.html', RedirectView.as_view(url='/gallery/', permanent=True)),
path('contact-us/shop.html', RedirectView.as_view(url='/shop/', permanent=True)),
path('contact-us/wishlist.html', RedirectView.as_view(url='/wishlist/', permanent=True)),
path('contact-us/index.html', RedirectView.as_view(url='/index/', permanent=True)),
 path('contact-us/checkout.html', views.checkout, name='contact_us_checkout'),
path('shop/my-account.html', RedirectView.as_view(url='/my-account/', permanent=True)),
 path('contact-us/contact-us.html', RedirectView.as_view(url='/contact-us/', permanent=True)),
path('contact-us/contact-us.html', RedirectView.as_view(url='/index/', permanent=True)),
path('checkout/checkout.html', RedirectView.as_view(url='/checkout/', permanent=True)),
path('checkout/index.html', RedirectView.as_view(url='/checkout/', permanent=True)),

    path('update-like/', views.update_like, name='update_like'),
    path('update-view/', views.update_view, name='update_view'),
    path('submit-comment/', views.submit_comment, name='submit_comment'),
]


