from django.db import models


class BaseMixinManagerActive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class BaseMixinManagerInactive(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=False)
