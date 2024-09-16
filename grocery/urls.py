"""
URL configuration for grocery project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Grocery_app import views
from django.contrib.auth import views as auth_views
#we are accessing the views file which is found in our application folder(Grocery_app)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='Grocery_app/login.html'), name='login'),
    path('', views.index, name='index'),
    path('logout/', views.log_out, name ='logout'),
    path('home/<int:product_id>/', views.product_detail, name='product_detail'),
    path('home/<int:product_id>/delete/', views.delete_detail, name='delete_detail'),
    path('delete/<int:product_id>/', views.delete_detail, name='delete_detail'),
    path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),
    path('receipt/', views.receipt, name='receipt'),
    path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
    path('all_sales/', views.all_sales, name='all_sales'),
    path('add_stock/<str:pk>/', views.add_stock, name='add_stock'),
    ]
