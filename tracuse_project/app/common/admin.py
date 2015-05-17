from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True

    list_display = ("__str__", "active", "sort")
    list_editable = ("active", "sort")
    list_display_links = ("__str__",)
    list_per_page = 12
    list_select_related = True

    fields = (("active", "sort"),)

    ordering = ["sort"]


class BaseModelInline(admin.TabularInline):
    fields = (("__str__", "active", "sort"),)
    readonly_fields = ("__str__", )

    extra = 1
    list_select_related = True
    show_change_link = True

    ordering = ["sort"]


class EntityModelAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True

    list_display = ("__str__", "active", "sort", "entity_name",
                    "short_definition", "long_definition", "example",
                    "readable_name", "readable_plural_name", "schema_name")
    list_editable = ("active", "sort", "entity_name",
                     "short_definition", "long_definition", "example",
                     "readable_name", "readable_plural_name", "schema_name")
    list_display_links = ("__str__",)
    list_per_page = 12
    list_select_related = True

    fields = (("active", "sort", "entity_name"),
              ("short_definition", "long_definition", "example"),
              ("readable_name", "readable_plural_name", "schema_name"),)

    ordering = ["sort"]


class EntityModelInline(admin.TabularInline):
    fields = ("__str__", "active", "sort", "entity_name",
              "short_definition", "long_definition",
              "readable_name", "readable_plural_name", "schema_name")
    readonly_fields = ("__str__", )
    extra = 1
    list_select_related = True
    show_change_link = True

    ordering = ["sort"]