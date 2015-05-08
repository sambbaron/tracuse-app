from django.contrib import admin


class BaseMixinAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True
    list_select_related = True

    list_display = ("__str__", "active", "sort")
    list_editable = ("active", "sort")
    list_display_links = ("__str__",)

    fields = (("active", "sort"),)

    ordering = ["sort"]


class BaseMixinInline(admin.TabularInline):
    fields = (("__str__", "active", "sort"),)
    readonly_fields = ("__str__", )

    extra = 1
    list_select_related = True
    show_change_link = True

    ordering = ["sort"]


class EntityMixinAdmin(admin.ModelAdmin):
    actions_on_top = True
    save_on_top = True

    list_select_related = True

    list_display = ("__str__", "active", "sort", "entity_name",
                    "short_definition", "long_definition",
                    "readable_name", "readable_plural_name", "schema_name")
    list_editable = ("active", "sort", "entity_name",
                     "short_definition", "long_definition",
                     "readable_name", "readable_plural_name", "schema_name")
    list_display_links = ("__str__",)

    fields = (("active", "sort", "entity_name"),
              ("short_definition", "long_definition"),
              ("readable_name", "readable_plural_name", "schema_name"),)

    ordering = ["sort"]


class EntityMixinInline(admin.TabularInline):
    fields = ("__str__", "active", "sort", "entity_name",
              "short_definition", "long_definition",
              "readable_name", "readable_plural_name", "schema_name")
    readonly_fields = ("__str__", )
    extra = 1
    list_select_related = True
    show_change_link = True

    ordering = ["sort"]