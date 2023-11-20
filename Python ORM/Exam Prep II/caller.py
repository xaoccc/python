import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions


from main_app.models import Product, Order, Profile

def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.filter(Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)).annotate(orders_num=Count("profile_order")).order_by("full_name")
    if not profiles:
        return ""

    result = []
    for p in profiles:
        result.append(f"Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_num}")

    return "\n".join(result)

def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()
    if not loyal_profiles:
        return ""

    result = []
    for p in loyal_profiles:
        result.append(f"Profile: {p.full_name}, orders: {p.orders_num}")

    return "\n".join(result)

def get_last_sold_products():
    latest_order = Order.objects.last()

    if not latest_order:
        return ""

    products_list = []
    for p in latest_order.products.all().order_by("name"):
        products_list.append(p.name)

    return f"Last sold products: {', '.join(products_list)}"

def get_top_products():
    products = Product.objects.prefetch_related("products_order").annotate(p_num=Count("products_order")).filter(p_num__gt=0).order_by("-p_num", "name")[:5]

    if not products:
        return ""

    result = ["Top products:"]
    for p in products:
        result.append(f"{p.name}, sold {p.p_num} times")

    return "\n".join(result)

def apply_discounts():
    orders = Order.objects.prefetch_related("products").annotate(p_num=Count("products")).filter(p_num__gt=2, is_completed=False)
    return f"Discount applied to {orders.update(total_price=F('total_price') * 0.9)} orders."

# Test code
# print(Profile.objects.get_regular_customers())

# print(get_profiles("V"))
# print(get_loyal_profiles())
# print(get_last_sold_products())

# print(get_top_products())
# print(apply_discounts())