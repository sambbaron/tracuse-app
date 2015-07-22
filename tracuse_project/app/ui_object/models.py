from django.db import models

from django.contrib.auth.models import User

from app.common.models import BaseModel, EntityModel


class UiObjectModel(BaseModel):
    """ Common properties/methods for UI Objects

    Attributes:
        See BaseModel
        user_id (integer, fk, nullable): User
            No user - global viewuse available to all users
        title (string)
        description (string)
        ui_arrangement_type_id (integer, fk, required):
            UiArrangementType - Used to relate to Arrangement options
        ui_arrangement_type_id (integer, fk, required):
            UiFormattingType - Used to relate to Formatting options
        datum_filter (string):
            JSON string of filter rules
            Correspond to FilterSet model
    """

    class Meta(BaseModel.Meta):
        abstract = True

    user = models.ForeignKey(User,
                             db_column="user_id",
                             null=True, blank=True,
                             db_index=True
                             )
    title = models.CharField(max_length=100,
                             null=True, blank=True
                             )
    description = models.CharField(max_length=255,
                                   null=True, blank=True
                                   )
    ui_arrangement_type = models.ForeignKey("ui_object.UiArrangementType",
                                            db_column="ui_arrangement_type_id",
                                            null=True, blank=True
                                            )
    ui_formatting_type = models.ForeignKey("ui_object.UiFormattingType",
                                           db_column="ui_formatting_type_id",
                                           null=True, blank=True
                                           )
    datum_filter = models.TextField(default="",
                                    null=True, blank=True,
                                    unique=False
                                    )

    def __str__(self):
        return self.title


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
