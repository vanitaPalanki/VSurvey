
from django.contrib import admin
from django.urls import path
from project import views

admin.site.site_header = "Survey Admin"
admin.site.site_title = "Survey Admin Portal"
admin.site.index_title = "Welcome to Survey"

urlpatterns = [
    path("", views.index, name='index'),
    path("surveyor", views.surveyor, name='surveyor'),
    path("survey", views.survey, name='survey'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("contact", views.contact, name='contact'),
    path("Dashboard", views.Dashboard, name='Dashboard'),
    path("cprofile", views.cprofile, name='cprofile'),
    path("companyinfo", views.companyinfo, name='companyinfo'),
    path("updateprofile2", views.updateprofile2, name='updateprofile2'),
    path("nproduct", views.nproductView.as_view(), name='nproduct'),
    path("productdetail", views.productdetail, name='productdetail'),
    path("userregister", views.userregister, name='userregister'),
    path("companysurvey", views.companysurvey, name='companysurvey'),
    path("usersurvey", views.usersurvey, name='usersurvey'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("register", views.RegisterView.as_view(), name='register'),
    path("logout", views.logout, name='logout'),
    path("dashbord", views.dashbord, name='dashbord'),
    path("profile", views.profile, name='profile'), 
    path("product", views.product, name='product'), 
    path("surveystats", views.surveystats, name='surveystats'),
    path("editprofile", views.EditprofileView.as_view(), name='editprofile'),
    path("updateprofile", views.Updateprofile, name='Updateprofile'),
    path("addProduct", views.AddProductView.as_view(), name='addProduct'),



]