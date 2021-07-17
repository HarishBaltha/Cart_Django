"""ProjectShop URL Configuration

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
from django.contrib import admin
from django.urls import path
from Appshop import views
from Appshop.views import AddToCartView, ManageCartView
from ProjectShop import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('register_up/', views.register_up, name="register_up"),
    path('login/', views.login, name="login"),
    path('login_up/', views.login_up, name="login_up"),
    path('admins/', views.admins, name="admins"),
    path('admin_up/', views.admin_up, name="admin_up"),
    path('homes/', views.homes, name="homes"),
    #path('totals/', views.totals, name="totals"),
    path('cart/', views.cart, name="cart"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('show/', views.show, name="show"),

    path('buy/', views.buy, name="buy"),
    path('home/', views.home, name="home"),
    path('category_save/', views.category_save, name="category_save"),
    path('add_product/', views.add_product, name="add_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('view_cat/', views.view_cat, name="view_cat"),
    path('view_prod/', views.view_prod, name="view_prod"),
    path('allproducts/', views.allproducts, name="allproducts"),
    path('product<slug:slug>/', views.ProductDetailView.as_view(), name="productdetail"),

    path('add-to-cart<int:pk>/', AddToCartView.as_view(), name="addtocart"),
    path('mycart/', views.MyCartView, name="mycart"),
    path('manage_cart<int:pk>/', ManageCartView.as_view(), name="managecart"),
    path('empty_cart/', views.EmptyCartView, name="emptycart"),
    path('profile/', views.profile, name="profile"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('adminlogin_up/', views.adminlogin_up, name="adminlogin_up"),
    #path('checkout/', views.CheckoutView, name="checkout"),
    #path('placeorder/', views.placeorder, name="placeorder"),
    #path('checkout/', CheckoutView.as_view(), name="checkout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
