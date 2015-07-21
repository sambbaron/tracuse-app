from django.contrib import admin

from app.ui_object.admin import UiObjectModelAdmin, UiObjectModelInline
from .models import ViewuseObject


class ViewuseObjectInline(UiObjectModelInline):
    model = ViewuseObject

    fields = UiObjectModelInline.fields


@admin.register(ViewuseObject)
class ViewuseObjectAdmin(UiObjectModelAdmin):
    list_display = UiObjectModelAdmin.list_display
    list_editable = UiObjectModelAdmin.list_editable

    fields = UiObjectModelAdmin.fields
