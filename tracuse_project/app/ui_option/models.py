from django.db import models

from app.common.models import BaseModel

class UiOptionModel(BaseModel):
    """ Common properties for UI Attribute Option Models

    Arrangement and Formatting Options

    Attributes:
        See BaseModel
        ui_object_id (integer, required):
            Loose Foreign Key to UI Object subclasses

    """

    class Meta(BaseModel.Meta):
        abstract = True

    ui_object_id = models.IntegerField()
