from django.db import models

from django.contrib.auth.models import User

from app.common.models import BaseModel, EntityModel


class ViewuseObject(EntityModel):
    """Primary View Object

    Attributes:
        See EntityModel
        user_id (integer, fk, nullable): User
            No user - global viewuse available to all users
        EntityModel.readable_name (string):
            Viewuse title
        viewuse_arrangement_id (integer, fk, required):
            ViewuseArrangement - Datum Placement Template
        viewuse_datum_id (integer, fk, required):
            ViewuseDatum - Datum Format Template
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


class ViewuseArrangement(EntityModel):
    """Placement of Datums within Viewuse

    Tie to client side viewuse templates

    Attributes:
        See EntityModel
        EntityModel.entity_name (string):
            Template name
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_arrangement"
        verbose_name = "Viewuse Arrangement Template"

    viewuse_arrangement_id = models.AutoField(primary_key=True)


class ViewuseDatum(EntityModel):
    """Format of Datums within Viewuse

    Tie to client side datum templates

    Attributes:
        See EntityModel
        EntityModel.entity_name (string):
            Template name
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_datum"
        verbose_name = "Viewuse Datum Template"

    viewuse_datum_id = models.AutoField(primary_key=True)


class ViewuseFilter(EntityModel):
    """Filters assigned to Viewuse Objects

    Use to generate template data
    ***Not sure whether filters should persist
        Use either json or FilterSet model

    Attributes:
        See EntityModel
        viewuse_object_id (integer, fk, required):
            ViewuseObject
        filter_json (string):
            JSON string of filter rules
        filter_set_id (integer, fk, required):
            FilterSet
    """

    class Meta(EntityModel.Meta):
        db_table = "viewuse_filter"
        verbose_name = "Viewuse Filter"

    viewuse_filter_id = models.AutoField(primary_key=True)
    viewuse_object = models.ForeignKey("viewuse.ViewuseObject",
                                       db_column="viewuse_object_id",
                                       related_name="viewuse_filters",
                                       null=False, blank=False
                                       )
    filter_json = models.CharField(max_length=255,
                                   default="",
                                   null=True, blank=True,
                                   unique=False
                                   )
    filter_set = models.ForeignKey("filter.FilterSet",
                                   db_column="filter_set_id",
                                   related_name="viewuse_filters",
                                   null=True, blank=True
                                   )


class ViewuseFormatting():
    pass
