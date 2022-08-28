
from django import forms
from project.models import register, profile, addProduct
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]

class RegisterForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = register
        fields = ['id', 'firstname', 'lastname', 'username', 'dob', 'gender', 'qualification', 'occupation', 'mobile_no', 'email']
        labels = {'firstname':'First Name', 'lastname':'Last Name', 'dob':'Date of Birth', 'mobile_no':'Mobile No.', 'email':'Email ID'}
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'qualification':forms.Select(attrs={'class':'form-select'}),
            'occupation':forms.Select(attrs={'class':'form-select'}),
            'mobile_no':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
class Profile(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = profile
        fields = ['user','companyname', 'dob', 'gender', 'userqualification', 'userdesignation', 'mobileno', 'profile_image', 'companydescription']
        labels = {'companyname':'Company Name', 'dob':'User DOB', 'gender':'Gender', 'userqualification':'User Qualification', 'userdesignation':'User Designation', 'mobileno':'Mobile No.', 'profile_image':'Upload Image', 'companydescription':'About company'}
        widgets = {
            'companyname':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'userqualification':forms.TextInput(attrs={'class':'form-control'}),
            'userdesignation':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_no':forms.NumberInput(attrs={'class':'form-control'}),            
            'companydescription':forms.Textarea(attrs={'class':'form-control', "rows":5,"cols":6}), 
        }
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        lables = {'username':'Username', 'email':'Email', 'first_name':'First Name', 'last_name':'Last Name'}
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['mobileno', 'profile_image', 'companydescription']
        lables = {'mabileno':'Mobile N0.', 'profile_image':'Profile Image', 'companydescription':'About Company'}
        widgets = {
            'mobile_no':forms.NumberInput(attrs={'class':'form-control'}),            
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'companydescription':forms.Textarea(attrs={'class':'form-control', "rows":5,"cols":6}), 
        }

class AddProductForm(forms.ModelForm):
    class Meta:
        model = addProduct
        fields = ['user', 'pname', 'ptype', 'pcategory', 'cost', 'best_before', 'preferred_consumer', 'packaging_Details', 'About_product', 'product_image'] 
        lables = {'pname':'Product_Name', 'ptype':'Product_Type', 'pcategory':'Product_Category', 'cost':'Cost', 'best_before':'Best_Before_Expire', 'preferred_consumer':'Prefered_Consumers','packaging_Details':'Packaging_Details', 'About_product':'About_Product_Details', 'product_image':'Product_image'}
        widgets = {
            'pname':forms.TextInput(attrs={'class':'form-control'}),
            'ptype':forms.TextInput(attrs={'class':'form-control'}),
            'pcategory':forms.Select(attrs={'class':'form-select'}),
            'cost':forms.NumberInput(attrs={'class':'form-control'}), 
            'best_before':forms.TextInput(attrs={'class':'form-control'}),
            'preferred_consumer':forms.Select(attrs={'class':'form-select'}),
            'packaging_Details':forms.Textarea(attrs={'class':'form-control', "rows":5,"cols":6}),
            'About_product':forms.Textarea(attrs={'class':'form-control', "rows":5,"cols":6}), 
        }