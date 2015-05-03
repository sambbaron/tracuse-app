from django.contrib import admin

from .models import ElementTypeDatumObject, ElementType
from components.element_value.admin import ElementValuesInline


class ElementTypeDatumObjectInline(admin.TabularInline):
    model = ElementTypeDatumObject

    fields = ("datum_object", "element_type", "element_value",)
    readonly_fields = ("element_value", )
    extra = 1
    list_select_related = True
    show_change_link = True


@admin.register(ElementTypeDatumObject)
class ElementTypeDatumObjectAdmin(admin.ModelAdmin):
    list_display = ("datum_object", "element_type", "element_value",)
    # list_editable = ("datum_object", "element_type", )
    list_display_links = ("element_value",)
    list_select_related = True

    inlines = [ElementValuesInline, ]
