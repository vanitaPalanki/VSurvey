from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import RegisterForm, Profile, UserUpdateForm, ProfileUpdateForm, AddProductForm
from .models import register, profile, addProduct
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("hello")

def surveyor(request):
    return render(request, 'surveyor.html')
    #return HttpResponse("hello")

def survey(request):
    return render(request, 'survey.html')

def aboutus(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Dashboard(request):
    return render(request, 'Dashboard.html')

def cprofile(request):
    return render(request, 'profile.html')

def companyinfo(request):
    return render(request, 'companyinfo.html')

def updateprofile2(request):
    return render(request, 'updateprofile2.html')

def productdetail(request):
    return render(request, 'productdetail.html')

class nproductView(View):
    def get(self, request):
        user = User.objects.all()
        addproduct = addProduct.objects.all()
        product = User.objects.all().prefetch_related('addproduct_set')
        return render(request, 'nproduct.html',{'product':product})

def userregister(request):
    return render(request, 'userregister.html')


def usersurvey(request):
    return render(request, 'usurvey.html')
    #return HttpResponse("UserSurvey")

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form':form}) 
    def post(self, request):
        form  = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/usersurvey')

class AddProductView(View):
    def get(self, request):
        form2 = AddProductForm()
        return render(request, 'add_product.html', {'form2':form2})
    def post(self, request):
        form2 = AddProductForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            return redirect('/product')



class EditprofileView(View):
    def get(self, request):
        form1 = Profile()
        return render(request, 'editprofile.html', { 'form1':form1})
    def post(self, request):
        form1 = Profile(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/profile')

def Updateprofile (request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form': p_form
    }

    return render(request, 'update_profile.html',context)

def companysurvey(request):
    return render(request, 'csurvey.html')
    #return HttpResponse("CompanySurvey")

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save();
                messages.info(request, 'Sucessfully Registered')
                return redirect('/login')
        else:
            print('password not matching..')
            messages.info(request, 'Password did not matched')
            return redirect('/signup')
         
    else:
        return render(request, 'signup.html')

    
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'sucessfully loged in')
            return redirect("/Dashboard")

        else:
            messages.info(request, 'invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'login.html') 

def logout(request):
    auth.logout(request)
    return redirect('/surveyor')

def dashbord(request):
    return render(request, 'dashbord.html')

def profile(request):
    return render(request, 'o_profile.html')

def product(request):
    return render(request, 'product.html')


def surveystats(request):
    return render(request, 'surveystats.html')

def editprofile(request):
    return render(request, 'editprofile.html')