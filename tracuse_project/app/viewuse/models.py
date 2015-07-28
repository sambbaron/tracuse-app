from django.db import models

from django.contrib.auth.models import User

from app.common.models import EntityModel, UiObjectModel


class ViewuseObject(UiObjectModel):
    """Primary View Object

    Attributes:
        See UiObjectModel
        viewuse_arrangement_id (integer, fk, required):
            ViewuseArrangement - Datum Placement View/Template
    """
    common_name = "View"

    class Meta(UiObjectModel.Meta):
        db_table = "viewuse_object"
        verbose_name = "Viewuse Object"
        default_related_name = "viewuse_objects"

    viewuse_object_id = models.AutoField(primary_key=True)
    viewuse_arrangement = models.ForeignKey("viewuse.ViewuseArrangement",
                                            db_column="viewuse_arrangement_id",
                                            null=False, blank=False
                                            )


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
