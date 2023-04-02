from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, phone, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    phone = models.BigIntegerField(max_length=10,unique=True, verbose_name='Phone Number', blank=False, help_text='Enter 10 digits phone number')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%M%D%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)

class Category(models.Model):
    slug = models.CharField(max_length=150, null =False, blank=False)
    name = models.CharField(max_length=150, null =False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null =True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0-default, 1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-hidden")
    meta_title =models.CharField(max_length=150, null=False, blank=False)
    meta_keywords =models.CharField(max_length=150, null=False, blank=False)
    meta_description =models.TextField(max_length=500, null=False, blank=False)
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null =False, blank=False)
    name = models.CharField(max_length=150, null =False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null =True, blank=True)
    
    small_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField( null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField( null=False, blank=False)
    selling_price = models.FloatField( null=False, blank=False)

    status = models.BooleanField(default=False, help_text="0-default, 1-hidden")
    trending = models.BooleanField(default=False, help_text="0-default, 1-hidden")
    tag=models.CharField(max_length=150, null=False, blank=False)
    meta_title =models.CharField(max_length=150, null=False, blank=False)
    meta_keywords =models.CharField(max_length=150, null=False, blank=False)
    meta_description =models.TextField(max_length=500, null=False, blank=False)  
    created_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        product_qty =models.IntegerField(null=False, blank=False)
        created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)
    lname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=150, null=False)
    phone = models.CharField(max_length=150, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=150, null=False)
    payment_id = models.CharField(max_length=250, null=False)
    orderstatuses =(
        ('pending', 'pending'),
        ('Out for Shipping', 'Out for Shipping'),
        ('Completed', 'Completed'),
    )
    
    status = models.CharField(max_length=250, choices=orderstatuses, default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True, default="Not available" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.lname)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    tracking_no = models.CharField(max_length=150, null=True)

    def __str__(self):
       return '{} - {}'.format(self.id, self.order.user.first_name, self.order.email)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)
    city = models.CharField(max_length=150, null=False)
    state = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=150, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.first_name
    