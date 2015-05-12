from django.contrib import admin

from app.common.admin import BaseMixinAdmin, BaseMixinInline, EntityMixinAdmin
from .models import ElementType, ElementTypeDatumType, ElementTypeDatumObject
from app.element_value.admin import ElementValuesInline


class ElementTypeDatumTypeAdmin(BaseMixinInline):
    model = ElementTypeDatumType

    fields = BaseMixinInline.fields + ("datum_type", "element_type")


class ElementTypeDatumObjectInline(BaseMixinInline):
    model = ElementTypeDatumObject

    fields = BaseMixinInline.fields + ("datum_object", "element_type", "element_value")
    readonly_fields = BaseMixinInline.readonly_fields + ("element_value", )


@admin.register(ElementTypeDatumObject)
class ElementTypeDatumObjectAdmin(BaseMixinAdmin):

    list_display = BaseMixinAdmin.list_display + ("datum_object", "element_type", "element_value")
    list_display_links = ("element_value",)

    fields = BaseMixinAdmin.fields + (("datum_object", "element_type"),)

    inlines = [ElementValuesInline, ]


@admin.register(ElementType)
class ElementTypeAdmin(EntityMixinAdmin):

    list_display = EntityMixinAdmin.list_display + ("element_data_type",)
    fields = EntityMixinAdmin.fields + ("element_data_type",)

    inlines = [ElementTypeDatumTypeAdmin, ]