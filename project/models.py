from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save 

# Create your models here.

class Signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    cpassword = models.CharField(max_length=50)

def __str__(self):
    return self.email

QUALIFICATION_CHOICES = (
    ('10th/12th','10th/12th'),
    ('Under_Graduate','Under_Graduate'),
    ('Post_Graduate','Post_Graduate'),
    ('PHD','PHD'),
)

OCCUPATION_CHOICES = [
    ('Home Maker','Home Maker'),
    ('Government Employee','Government Employee'),
    ('Artist','Artist'),
    ('Social Worker','Social Worker'),
    ('Freelencer','Freelencer'),
    ('Designer','Designer'),
    ('Enterpreneur','Enterpreneur'),
    ('Other','Other'),
]

PRODUCT_CATEGORY_CHOICES = [
    ('Spices', 'Spices'),
    ('Chocklets', 'Chocklets'),
    ('Beverages', 'Beverages'),
    ('Tea & Coffee', 'Tea & Coffee'),
    ('Processed Fish', 'Processed Fish'),
    ('Processed oils', 'Processed oils'),
    ('Processed Meats', 'Processed Meats'),
    ('Bakery Products', 'Bakery Products'),
    ('Chips & Waffers', 'Chips & Waffers'),
    ('Processed Grains', 'Processed Grains'),
    ('Pastas & Noodles', 'Pastas & Noodles'),
    ('Milk & Milk Products', 'Milk & Milk Products'),
    ('Processed Sugar & Salt', 'Processed Sugar & Salt'),
    ('Packaged Fruits & Vegitables', 'Packaged Fruits & Vegitables'),
    ('Non of the above', 'Non of the above'),
]

PREFFERED_CONSUMER_CHOICES = [
    ('All', 'All'),
    ('Infant/Newborn', 'Infant/Newborn'),
    ('Below 5 years', 'Below 5 years'),
    ('5 to 18 years', '5 to 18 years'),
    ('Above 18', 'Above 18'),
    ('Senior Citizen', 'Senior Citizen'),
] 

class register(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50)
    qualification = models.CharField(choices=QUALIFICATION_CHOICES,max_length=50)
    occupation = models.CharField(choices=OCCUPATION_CHOICES,max_length=50)
    mobile_no = models.PositiveIntegerField()
    email = models.EmailField() 


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default="")
    companyname = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    userqualification = models.CharField(max_length=50)
    userdesignation = models.CharField(max_length=50)
    mobileno = models.PositiveIntegerField()
    profile_image = models.ImageField(upload_to='profileimg/', blank=True)
    companydescription = models.TextField(default="")

class addProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pname = models.CharField(max_length=200)
    ptype = models.CharField(max_length=200)
    pcategory = models.CharField(choices=PRODUCT_CATEGORY_CHOICES , max_length=50)
    cost = models.PositiveIntegerField()
    best_before = models.CharField(max_length=100)
    preferred_consumer = models.CharField(choices=PREFFERED_CONSUMER_CHOICES, max_length=100)
    packaging_Details = models.TextField()
    About_product = models.TextField()
    product_image = models.ImageField(upload_to='productimg/', blank=True)

