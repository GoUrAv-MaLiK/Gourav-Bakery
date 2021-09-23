"""gouravbakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cart import  views_cart
from customer import views_customer
from shipping_and_billing import views_shipment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views_customer.registerPage, name="register"),
	path('login/', views_customer.loginPage, name="login"),  
	path('logout/', views_customer.logoutUser, name="logout"),
	path("",views_customer.loginPage),
    path("home/",views_cart.Product_display),
    path("shipment/",views_shipment.Shipping_and_billing,name="shipment"),
    path("handlepayment/",views_shipment.handlepayment)
    
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
