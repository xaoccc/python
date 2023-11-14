from django.db import models
from django.db.models import Count

class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        result = []
        for item in self.all().annotate(movies_num=Count("movie__director")).order_by("-movies_num", "full_name"):
            result.append(item.full_name)
        return result
