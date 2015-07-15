from django.db import models

from django.contrib.auth.models import User

from app.common.models import BaseModel, EntityModel


class ViewuseObject(BaseModel):
    """Primary View Object

    Attributes:
        See BaseModel
        user_id (integer, fk, nullable): User
            No user - global viewuse available to all users
        title (string)
        description (string)
        viewuse_arrangement_id (integer, fk, required):
            ViewuseArrangement - Datum Placement View/Template
        viewuse_datum_id (integer, fk, required):
            ViewuseDatum - Datum Format View/Template
        viewuse_filter (string):
            JSON string of filter rules
            Correspond to FilterSet model
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_object"
        verbose_name = "Viewuse Object"

    viewuse_object_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,
                             db_column="user_id",
                             related_name="viewuse_objects",
                             null=True, blank=True,
                             db_index=True
                             )
    title = models.CharField(max_length=100,
                             null=True, blank=True
                             )
    description = models.CharField(max_length=255,
                                   null=True, blank=True
                                   )
    viewuse_arrangement = models.ForeignKey("viewuse.ViewuseArrangement",
                                            db_column="viewuse_arrangement_id",
                                            related_name="viewuse_objects",
                                            null=False, blank=False
                                            )
    viewuse_datum = models.ForeignKey("viewuse.ViewuseDatum",
                                      db_column="viewuse_datum_id",
                                      related_name="viewuse_objects",
                                      null=False, blank=False
                                      )
    viewuse_filter = models.TextField(default="",
                                      null=True, blank=True,
                                      unique=False
                                      )

    def __str__(self):
        return self.title


class ViewuseArrangement(EntityModel):
    """Placement of Datums within Viewuse

    Tie to client side viewuse view/template

    Attributes:
        See EntityModel
        EntityModel.entity_name (string):
            View/Template name
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_arrangement"
        verbose_name = "Viewuse Arrangement"

    viewuse_arrangement_id = models.AutoField(primary_key=True)


class ViewuseDatum(EntityModel):
    """Format of Datums within Viewuse

    Tie to client side datum view/template

    Attributes:
        See EntityModel
        EntityModel.entity_name (string):
            View/Template name
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_datum"
        verbose_name = "Viewuse Datum"

    viewuse_datum_id = models.AutoField(primary_key=True)


class ViewuseFormatting():
    pass


class ViewuseNested(BaseModel):
    """Viewuses spatially nested within Viewuses

    Attributes:
        See BaseModel
        parent_viewuse_id (integer, pk, fk): ViewuseObject
        nested_viewuse_id (integer, pk, fk): ViewuseObject
        order (integer): relative to parent Datum content
            used for positioning
            example: -1 -> before datums
                      1 -> after datums
        height (string): CSS height
        width (string): CSS width
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_nested"
        verbose_name = "Nested Viewuse"
        verbose_name_plural = "Nested Viewuses"

    viewuse_nested_id = models.AutoField(primary_key=True)
    parent_viewuse = models.ForeignKey("viewuse.ViewuseObject",
                                       db_column="parent_viewuse_id",
                                       related_name="nested_viewuses",
                                       null=False, blank=False
                                       )
    nested_viewuse = models.ForeignKey("viewuse.ViewuseObject",
                                       db_column="nested_viewuse_id",
                                       related_name="parent_viewuses",
                                       null=False, blank=False
                                       )
    order = models.IntegerField(default=1,
                                null=False, blank=False
                                )
    height = models.CharField(max_length=4, default="auto",
                              null=False, blank=False
                              )
    width = models.CharField(max_length=4, default="auto",
                             null=False, blank=False
                             )

    def __str__(self):
        return "{} -> {}".format(
            self.parent_viewuse.__str__(),
            self.nested_viewuse.__str__()
        )
