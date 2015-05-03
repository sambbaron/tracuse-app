from django.contrib import admin

from .models import DatumType, DatumObject
from components.element_type.admin import ElementTypeDatumObjectInline


class DatumObjectInline(admin.TabularInline):
    model = DatumObject

    fields = (("__str__", "active", "sort"),)
    readonly_fields = ("__str__", )
    extra = 1
    list_select_related = True
    show_change_link = True


@admin.register(DatumType)
class DatumTypeAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True
    list_select_related = True

    list_display = ("__str__", "active", "sort", "entity_name",
                    "short_definition", "long_definition",
                    "repr_expression",
                    "readable_name", "readable_plural_name", "schema_name")
    list_editable = ("active", "sort", "entity_name",
                     "short_definition", "long_definition",
                     "repr_expression",
                     "readable_name", "readable_plural_name", "schema_name")
    list_display_links = ("__str__",)

    fields = (("active", "sort", "entity_name"),
              ("short_definition", "long_definition"),
              ("repr_expression"),
              ("readable_name", "readable_plural_name", "schema_name"),)

    inlines = [DatumObjectInline, ]


@admin.register(DatumObject)
class DatumObjectAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True
    list_select_related = True

    list_display = ("__str__", "user", "active", "sort", "datum_type", "datum_group")
    list_editable = ("user", "active", "sort", "datum_type")

    fields = (("user", "active", "sort", "datum_type"),)
    readonly_fields = ("element_types",)

    inlines = [ElementTypeDatumObjectInline, ]
