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
        ui_arrangement_options (calculated property):
            UiArrangement* model object
        ui_formatting_options (calculated property):
            UiFormatting* model object
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
    ui_arrangement_type = models.ForeignKey("ui_arrangement.UiArrangementType",
                                            db_column="ui_arrangement_type_id",
                                            null=True, blank=True
                                            )
    ui_formatting_type = models.ForeignKey("ui_formatting.UiFormattingType",
                                           db_column="ui_formatting_type_id",
                                           null=True, blank=True
                                           )
    datum_filter = models.TextField(default="",
                                    null=True, blank=True,
                                    unique=False
                                    )

    def _ui_option_model(self, attribute_type):
        """ Return UI option model

        Create if doesn't exist

        Parameters:
            attribute_type (string): 'Arrangement' or 'Formatting'
        """

        type_class = globals()["Ui" + attribute_type + "Type"]
        type_property = locals()["ui_" + attribute_type.lower() + "type"]
        option_class = UiOptionMeta(attribute_type, type_property.entity_name)

        if type_class and type_property and option_class:
            option_model = option_class.objects.filter(
                ui_object_id=self.pk
            ).first()

            if not option_model:
                # Delete records in other option models
                for type_model in type_class.objects.all():
                    option_model_class = UiOptionMeta(attribute_type, type_model.entity_name)
                    if option_model_class:
                        option_model_class.objects.filter(ui_object_id=self.pk).delete()

                option_model = option_class.create(ui_object_id=self.pk)

            return option_model

    @property
    def ui_arrangement_options(self):
        return self._ui_option_model("Arrangement")

    @property
    def ui_formatting_options(self):
        return self._ui_option_model("Formatting")

    def delete(self, using=None):
        self.ui_arrangement_options.delete()
        self.ui_formatting_options.delete()
        super().delete(using)


class UiOptionMeta(object):
    """Factory class for UiOption models

    Model Name = "Ui" + Attribute Name + Type Name

    Attributes:
        attribute_name (string)
        type_name (string)
    """

    def __new__(cls, attribute_name, type_name):
        option_model_name = "Ui" + attribute_name + type_name
        try:
            return globals()[option_model_name]
        except KeyError:
            raise NameError("{} model class does not exist".format(option_model_name))


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