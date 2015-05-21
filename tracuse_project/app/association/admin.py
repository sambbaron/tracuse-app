from django.contrib import admin

from .models import AssociationAdjacent, AssociationAll


@admin.register(AssociationAdjacent)
class AssociationAdjacentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "parent_datum", "child_datum", "association_type")
    list_editable = ("parent_datum", "child_datum", "association_type")

    fields = ("parent_datum", "child_datum", "association_type")

@admin.register(AssociationAll)
class AssociationAllAdmin(admin.ModelAdmin):
    list_display = ("__str__", "parent_datum", "child_datum", "distance")
