from django.shortcuts import render, redirect
from Appshop.models import RegisterModel, LoginModel, AdminModel, Category, Cart, CartProduct, Product, Order
from django.contrib import messages
from django.views.generic import TemplateView, DetailView, View, CreateView
from Appshop.forms import CheckoutForm


def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def register_up(request):
    name = request.POST.get("r1")
    username = request.POST.get("r2")
    mail = request.POST.get("r3")
    contact = request.POST.get("r4")
    password = request.POST.get("r5")
    address = request.POST.get("r6")
    match = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    match1 = "abcdefghijklmnopqrstuvwxyz"
    integer = "1234567890"
    spl_chr = "!@#$%^&*"
    for x in password:
        if x in spl_chr:
            for y in password:
                if y in match:
                    for z in password:
                        if z in match1:
                            for a in password:
                                if a in integer:
                                    if len(str(password)) > 7 and len(str(password)) < 17:
                                        if len(str(contact)) == 10:
                                            RegisterModel(Name=name, Username=username, Email=mail, Contact=contact,
                                                Password=password, Address=address).save()
                                            LoginModel(Username=username, Password=password).save()
                                            messages.success(request, "Registered Successfully")
                                            return redirect("register")
                                        else:
                                            return render(request, "register.html", {"error": "Invalid Contact Number"})
                                    else:
                                        return render(request, "register.html", {"error5": "Password should be between 7 and 17 characters"})
                            else:
                                return render(request, "register.html", {"error4": "Choose atleast one Integer"})
                    else:
                        return render(request, "register.html", {"error3": "Choose atleast one Small Alphabet"})
            else:
                return render(request, "register.html", {"error2": "Choose atleast one Caps Alphabet"})
    else:
        return render(request, "register.html", {"error1": "Choose atleast one Special Character from !,@,#,$,%,^,&,*"})


def login(request):
    return render(request, "login.html")

def login_up(request):
    username = request.POST.get("l1")
    password = request.POST.get("l2")
    view = AdminModel.objects.all()
    try:
        LoginModel.objects.get(Username=username, Password=password)
        return render(request, "homes.html", {"data2": Product.objects.all(), "name": username})
    except LoginModel.DoesNotExist:
        return render(request, "login.html", {"error": "Username and Password doesn't match"})

def admins(request):
    return render(request, "Admin.html")

def admin_up(request):
    no = request.POST.get("d1")
    name = request.POST.get("d2")
    design = request.POST.get("d3")
    upload = request.FILES["d4"]
    cost = request.POST.get("d5")
    AdminModel(No=no, Name=name, Design=design, File=upload, Cost=cost).save()
    messages.success(request, "Uploades Successfully")
    return render(request, "Admin.html")

def homes(request):
    return render(request, "homes.html")

def cart(request):
    return render(request, "cart.html")

def save_cart(request):
    a1 = request.GET.get("pno")
    a2 = request.GET.get("pname")
    response = redirect("homes")
    if len(request.COOKIES) != 100:
        response.set_cookie(a1, a2, max_age=180)
        return response
    else:
        messages.error(request, "You are more about in cart")
        return redirect("homes")

def show(request):
    return render(request, "show.html", {"data3": request.COOKIES})

def buy(request):
    return render(request, "buy.html")

#def navbar1(request):
#    no_cookies = len(request.COOKIES)
#    return render(request, "navbar1.html", {"data2": no_cookies})

def home(request):
    return render(request, "home.html")

def category_save(request):
    tit = request.POST.get("c1")
    slu = request.POST.get("c2")
    Category(title=tit, slug=slu).save()
    messages.success(request, "Success")
    return redirect("home")

def add_product(request):
    return render(request, "add_product.html", {"data": Category.objects.all()})

def save_product(request):
    tit = request.POST.get("p1")
    slu = request.POST.get("p2")
    cate = request.POST.get("p3")
    imag = request.FILES["p4"]
    m_price = request.POST.get("p5")
    s_price = request.POST.get("p6")
    desc = request.POST.get("p7")
    warra = request.POST.get("p8")
    r_policy = request.POST.get("p9")
    Product(title=tit, slug=slu, category_id=cate, image=imag, marked_price=m_price, selling_price=s_price,
            description=desc, warranty=warra, return_policy=r_policy).save()
    messages.success(request, "Success")
    return redirect("add_product")

def view_cat(request):
    return render(request, "view_category.html", {"data1": Category.objects.all()})

def view_prod(request):
    return render(request, "admin_login.html", {"data2": Product.objects.all()})

def allproducts(request):
    return render(request, "allproducts.html", {"allcategory": Category.objects.all()}) #.order_by("-id") This is placing new added items at first place. (This Code is given after Category.objecta.all().order_by("-id)#

class ProductDetailView(DetailView):
    template_name = "productdetail.html"
    model = Product

class AddToCartView(TemplateView):
    template_name = "addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs["pk"]
        product_obj = Product.objects.get(no=product_id)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(product=product_obj)
            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
                # new item is added in cart
            else:
                cartproduct = CartProduct.objects.create(cart=cart_obj, product=product_obj,
                                                         rate=product_obj.selling_price, quantity=1,
                                                         subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(cart=cart_obj, product=product_obj, rate=product_obj.selling_price,
                                                     quantity=1, subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save()
        return context



def MyCartView(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = None
    return render(request, "mycart.html", {"cart": cart})
#            OR
#class MyCartView(TemplateView):
#    template_name = "mycart.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        cart_id = self.request.session.get("cart_id", None)
#        if cart_id:
#            cart = Cart.objects.get(id=cart_id)
#        else:
#            cart = None
#        context['cart'] = cart
#        return context

# As we used session, so cart items will be saved and not deleted. As this cart items are
# saved to database


class CheckoutView(CreateView):
    template_name = "checkout.html"
    form_class = CheckoutForm
    success_url = "/view_prod/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get("cart_id")
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            form.instance.cart = cart
            form.instance.subtotal = cart.total
            form.instance.discount = 0
            form.instance.total = cart.total
            form.instance.order = "order Received"
            del self.request.session['cart_id']
        else:
            return redirect("view_prod")
        return super().form_valid(form)

class ManageCartView(View):
    def get(self, request, *args, **kwargs):
        cp_id = self.kwargs["pk"]
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart
        if action == "inc":
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == "dcr":
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()
        elif action == "rmv":
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        return redirect("mycart")

def EmptyCartView(request):
    cart_id = request.session.get("cart_id")
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        cart.cartproduct_set.all().delete()
        cart.total = 0
        cart.save()
    return redirect("mycart")

def profile(request):
    un = request.GET.get("un")
    profile = RegisterModel.objects.get(Username=un)
    return render(request, "profile.html", {"name": un, "profile": profile})

def admin_login(request):
    return render(request, "admin_login.html")

def adminlogin_up(request):
    user = request.POST.get("a1")
    password = request.POST.get("a2")
    try:
        AdminModel.objects.get(Username=user, Password=password)
        return render(request, "buy.html")
    except AdminModel.DoesNotExist:
        messages.error(request, "Invalid Details")
        return redirect("admin_login")
