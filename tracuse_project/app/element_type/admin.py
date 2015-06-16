from django.contrib import admin

from app.common.admin import BaseModelAdmin, BaseModelInline, EntityModelAdmin, EntityModelInline
from .models import ElementType, ElementDatumType, ElementDatumObject, ElementOperator
from app.element_value.admin import ElementValuesInline


class ElementDatumTypeInline(EntityModelInline):
    model = ElementDatumType

    fields = EntityModelInline.fields + ("datum_type", "element_type", "calc_expression", "primary_view",)


class ElementDatumObjectInline(BaseModelInline):
    model = ElementDatumObject

    fields = BaseModelInline.fields + ("datum_object", "element_type", "element_value")
    readonly_fields = BaseModelInline.readonly_fields + ("element_value", )


@admin.register(ElementDatumType)
class ElementDatumTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display + ("datum_type", "element_type", "calc_expression", "primary_view",)
    list_editable = EntityModelAdmin.list_editable + ("datum_type", "element_type", "calc_expression", "primary_view",)
    list_filter = ("datum_type", "element_type", "calc_expression",)

    fields = EntityModelAdmin.fields + ("datum_type", "element_type", "calc_expression", "primary_view",)


@admin.register(ElementDatumObject)
class ElementDatumObjectAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + ("datum_object", "element_type", "element_value")
    list_display_links = ("element_value",)
    list_filter = ("datum_object", "element_type", )

    fields = BaseModelAdmin.fields + (("datum_object", "element_type"),)

    inlines = [ElementValuesInline, ]


@admin.register(ElementType)
class ElementTypeAdmin(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display + ("element_data_type", "str_expression", "element_view",)
    list_editable = EntityModelAdmin.list_editable + ("element_data_type", "str_expression", "element_view",)
    list_filter = ("element_data_type", )

    fields = EntityModelAdmin.fields + ("element_data_type", "str_expression", "element_view",)

    inlines = [ElementDatumTypeInline, ]

@admin.register(ElementOperator)
class ElementOperator(EntityModelAdmin):
    list_display = EntityModelAdmin.list_display + ("element_data_type", "default_operator", )
    list_editable = EntityModelAdmin.list_editable + ("element_data_type", "default_operator", )
    list_filter = ("element_data_type", )

    fields = EntityModelAdmin.fields + ("element_data_type", "default_operator", )