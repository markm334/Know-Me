from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password
from decimal import Decimal

class FarmerManager(BaseUserManager):
    def create_user(self, name, email, phone_number, location, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        farmer = self.model(name=name, email=email, phone_number=phone_number, location=location, **extra_fields)
        farmer.set_password(password)
        farmer.save(using=self._db)
        return farmer

    def create_superuser(self, name, email, phone_number, location, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(name, email, phone_number, location, password, **extra_fields)

class Farmer(PermissionsMixin, models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    location = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'phone_number', 'location']

    objects = FarmerManager()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    deposit_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0'))
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)