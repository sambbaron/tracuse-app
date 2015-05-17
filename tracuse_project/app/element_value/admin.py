from django.contrib import admin

from .models import ElementValueMeta


class ElementValuesInline(admin.TabularInline):
    model = ElementValueMeta("String")

