from django.contrib import admin

from components.datum.models import DatumObject
from components.element_type.models import ElementTypeDatumObject, ElementType
from components.element_value.models import ElementValueModel

class ElementTypeInline(admin.TabularInline):
    model = ElementTypeDatumObject

    fields = (("active", "sort", "element_type", "element_value"), )
    readonly_fields = ("element_value",)
    extra = 1
    list_select_related = True
    show_change_link = True


@admin.register(DatumObject)
class DatumAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True
    list_select_related = True

    list_display = ("__str__", "user", "active", "sort", "datum_type", "datum_group")
    list_editable = ("user", "active", "sort", "datum_type")

    fields = (("user", "active", "sort", "datum_type"),)
    readonly_fields = ("element_types",)

    inlines = [ElementTypeInline, ]


class ElementValuesInline(admin.TabularInline):
    model = ElementValueModel("String")

@admin.register(ElementTypeDatumObject)
class ElementTypeDatumObjectAdmin(admin.ModelAdmin):
    pass
    # inlines = [ElementValuesInline, ]
