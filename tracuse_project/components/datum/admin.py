from django.contrib import admin

from utils.admin import BaseMixinAdmin, BaseMixinInline, EntityMixinAdmin
from .models import DatumType, DatumObject
from components.element_type.admin import ElementTypeDatumObjectInline


class DatumObjectInline(BaseMixinInline):
    model = DatumObject


@admin.register(DatumObject)
class DatumObjectAdmin(BaseMixinAdmin):

    list_display = BaseMixinAdmin.list_display + ("user", "datum_type", "datum_group")
    list_editable = BaseMixinAdmin.list_editable + ("user", "datum_type")

    fields = BaseMixinAdmin.fields + ("user", "datum_type")
    readonly_fields = BaseMixinAdmin.readonly_fields + ("element_types",)

    inlines = [ElementTypeDatumObjectInline, ]


@admin.register(DatumType)
class DatumTypeAdmin(EntityMixinAdmin):

    list_display = EntityMixinAdmin.list_display + ("repr_expression", )
    list_editable = EntityMixinAdmin.list_editable + ("repr_expression", )

    fields = EntityMixinAdmin.fields + ("repr_expression", )

    inlines = [DatumObjectInline, ]