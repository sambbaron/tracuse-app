from django.contrib import admin

from components.datum.models import DatumObject
from components.element_type.models import ElementTypeDatumObject


class ElementTypeInline(admin.StackedInline):
    model = ElementTypeDatumObject
    extra = 0
    list_select_related = True
    show_change_link = True
    fields = ("element_type", "element_value" )
    readonly_fields = ("element_type", "element_value")
    can_delete = False


@admin.register(DatumObject)
class DatumAdmin(admin.ModelAdmin):

    actions_on_top = True
    save_on_top = True
    list_select_related = True

    list_display = ("__str__", "user", "active", "sort", "datum_type", "datum_group", "assigned_element_types")
    list_editable = ("user", "active", "sort", "datum_type")
    list_display_links = ("assigned_element_types",)

    fields = (("user", "active", "sort", "datum_type"))
    # readonly_fields = ("assigned_element_types",)

    # inlines = [ElementTypeInline, ]
