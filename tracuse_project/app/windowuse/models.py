from django.db import models

from django.contrib.auth.models import User

from app.common.models import BaseModel, UiObjectModel


class WindowuseObject(UiObjectModel):
    """Top-Level UI Object - Container for Viewuses

    Attributes:
        See UiObjectModel
    """

    class Meta(UiObjectModel.Meta):
        db_table = "windowuse_object"
        verbose_name = "Windowuse Object"
        default_related_name = "windowuse_objects"

    windowuse_object_id = models.AutoField(primary_key=True)


class WindowuseViewuse(BaseModel):
    """Viewuses inside Windowuse

    Can have Windowuse-specific ui attributes

    Attributes:
        See BaseModel
        windowuse_object_id (integer, fk, required):
            WindowuseObject
        viewuse_object_id (integer, fk, required):
            ViewuseObject
        sort (integer, from BaseModel):
            Use for rendering order
    """

    class Meta(BaseModel.Meta):
        db_table = "windowuse_viewuse"
        verbose_name = "Windowuse Viewuse"
        default_related_name = "windowuse_viewuses"

    windowuse_viewuse_id = models.AutoField(primary_key=True)
    windowuse_object = models.ForeignKey("windowuse.WindowuseObject",
                                         db_column="windowuse_object_id",
                                         null=False, blank=False
                                         )
    viewuse_object = models.ForeignKey("viewuse.ViewuseObject",
                                       db_column="viewuse_object_id",
                                       null=False, blank=False
                                       )

    def __str__(self):
        return "{} => {}".format(self.windowuse_object.__str__(),
                                 self.viewuse_object.__str__()
                                 )
