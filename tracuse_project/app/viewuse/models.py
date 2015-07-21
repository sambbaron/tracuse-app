from django.db import models

from django.contrib.auth.models import User

from app.common.models import BaseModel
from app.ui_object.models import UiObjectModel


class ViewuseObject(UiObjectModel):
    """Primary View Object

    Attributes:
        See UiObjectModel
    """

    class Meta(UiObjectModel.Meta):
        db_table = "viewuse_object"
        verbose_name = "Viewuse Object"
        default_related_name = "viewuse_objects"

    viewuse_object_id = models.AutoField(primary_key=True)
