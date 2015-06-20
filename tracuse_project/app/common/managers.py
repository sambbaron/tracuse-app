from django.db import models


class BaseModelManagerActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class BaseModelManagerInactive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=False)
