from django.contrib import admin

from .models import ElementValueModel


class ElementValuesInline(admin.TabularInline):
    model = ElementValueModel("String")

