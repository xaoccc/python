from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):
    def get_regular_customers(self):
        return self.all().annotate(orders_num=Count("profile_order")).filter(orders_num__gt=2).order_by("-orders_num")