from django.db import models

from app.common.models import EntityModel
from app.ui_option.models import UiOptionModel


class UiArrangementType(EntityModel):
    """Display/Positioning of objects within container

    Relate to Front-End UI attributes
    Examples: Flexbox, Graph, Calendar

    Attributes:
        See EntityModel
        entity_name: technical attribute name
            Correspond to UiArrangement* option model
            and client view/template name
        readable_name: user interface name
    """

    class Meta(EntityModel.Meta):
        db_table = "ui_arrangement_type"
        verbose_name = "Arrangement Type"

    ui_arrangement_type_id = models.AutoField(primary_key=True)


class UiArrangementTile(UiOptionModel):
    """ CSS Flexbox options for Display Objects

    Attributes:
        See UiOptionModel
        directon (string): flex-direction
        wrap (boolean): flex-wrap
    """

    class Meta(UiOptionModel.Meta):
        db_table = "ui_arrangement_tile"
        verbose_name = "Arrangement Tile Option"

    ui_arrangement_tile_id = models.AutoField(primary_key=True)
    direction = models.CharField(max_length=10, default="column",
                                 null=False, blank=False
                                 )
    wrap = models.BooleanField(default=False)

