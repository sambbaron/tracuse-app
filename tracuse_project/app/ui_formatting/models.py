from django.db import models

from app.common.models import EntityModel
from app.ui_object.models import UiOptionModel


class UiFormattingType(EntityModel):
    """Sets of object formatting options

    Attributes:
        See EntityModel
        entity_name: technical attribute name
            Must correspond to UiFormatting* model
        readable_name: user interface name
    """

    class Meta(EntityModel.Meta):
        db_table = "ui_formatting_type"
        verbose_name = "Formatting Type"

    ui_formatting_type_id = models.AutoField(primary_key=True)


class UiFormattingGeneric(UiOptionModel):
    """ Formatting Options for UI Objects
    """

    class Meta(UiOptionModel.Meta):
        db_table = "ui_formatting_generic"
        verbose_name = "Formatting Generic Options"
        verbose_name_plural = "Formatting Generic Options"

    ui_formatting_generic_id = models.AutoField(primary_key=True)
