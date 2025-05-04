from django import forms
from crudapp.models import Farmer, Product, Wishlist
from .models import Booking

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'deposit_percentage', 'image']  # added 'image'

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['product']

class FarmerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Farmer
        fields = ['name', 'email', 'phone_number', 'location', 'password']
    
    def save(self, commit=True):
        farmer = super().save(commit=False)
        farmer.set_password(self.cleaned_data["password"])
        if commit:
            farmer.save()
        return farmer

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'location', 'phone_number', 'email', 'quantity']  # added 'quantity'