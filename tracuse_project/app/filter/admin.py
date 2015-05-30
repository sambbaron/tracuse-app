from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import FilterSet


class FilterSetInline(EntityModelInline):
    model = FilterSet

    fields = EntityModelInline.fields


@admin.register(FilterSet)
class FilterSetAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display
    list_editable = EntityModelAdmin.list_editable

    fields = EntityModelAdmin.fields