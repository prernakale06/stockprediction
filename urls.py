from django.urls import path,include
from .import views


urlpatterns = [
   path("", views.home, name="home"),
   path("about.html", views.about, name="about"),
   path("add_stock.html", views.add_stock, name="add_stock"),
   path("delete/<stock_id>", views.delete, name="delete"),
   path("delete_stock.html", views.delete_stock, name="delete_stock"),
   path("registration/login/.html", views.login, name="login"),
   path("ustock.html", views.ustock, name="ustock"),
   # path("dashboard.html",views.dashboard, name="dashboard"),
   path("main.html",views.main,name="main"),
   path("contact.html",views.contact,name="contact"),
   path("calculator.html",views.calculator,name="calculator"),
   path("accounts/",include('accounts.urls')),
   
]

