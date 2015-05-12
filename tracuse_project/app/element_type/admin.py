from django.contrib import admin

from app.common.admin import BaseMixinAdmin, BaseMixinInline, EntityMixinAdmin
from .models import ElementType, ElementDatumType, ElementDatumObject
from app.element_value.admin import ElementValuesInline


class ElementDatumTypeInline(BaseMixinInline):
    model = ElementDatumType

    fields = BaseMixinInline.fields + ("datum_type", "element_type")


class ElementDatumObjectInline(BaseMixinInline):
    model = ElementDatumObject

    fields = BaseMixinInline.fields + ("datum_object", "element_type", "element_value")
    readonly_fields = BaseMixinInline.readonly_fields + ("element_value", )


@admin.register(ElementDatumType)
class ElementDatumTypeAdmin(BaseMixinAdmin):

    list_display = BaseMixinAdmin.list_display + ("datum_type", "element_type", "calc_expression",)
    list_editable = BaseMixinAdmin.list_editable + ("datum_type", "element_type", "calc_expression",)
    list_filter = ("datum_type", "element_type", "calc_expression",)

    fields = BaseMixinAdmin.fields + ("datum_type", "element_type")


@admin.register(ElementDatumObject)
class ElementDatumObjectAdmin(BaseMixinAdmin):

    list_display = BaseMixinAdmin.list_display + ("datum_object", "element_type", "element_value")
    list_display_links = ("element_value",)
    list_filter = ("datum_object", "element_type", )

    fields = BaseMixinAdmin.fields + (("datum_object", "element_type"),)

    inlines = [ElementValuesInline, ]


@admin.register(ElementType)
class ElementTypeAdmin(EntityMixinAdmin):

    list_display = EntityMixinAdmin.list_display + ("element_data_type",)
    list_editable = EntityMixinAdmin.list_editable + ("element_data_type",)
    fields = EntityMixinAdmin.fields + ("element_data_type",)

    inlines = [ElementDatumTypeInline, ]