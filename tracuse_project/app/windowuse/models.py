from django.db import models

from django.contrib.auth.models import User

from app.common.models import BaseModel


class WindowuseObject(BaseModel):
    """App Window Object - Container for Viewuses

    Attributes:
        See BaseModel
        user_id (integer, fk, nullable): User
            No user - global viewuse available to all users
        title (string)
        description (string)
    """

    class Meta(BaseModel.Meta):
        db_table = "windowuse_object"
        verbose_name = "Windowuse Object"
        default_related_name = "windowuse_objects"

    windowuse_object_id = models.AutoField(primary_key=True)
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
    datum_filter = models.TextField(default="",
                                    null=True, blank=True,
                                    unique=False
                                    )

    def __str__(self):
        return self.title


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
