
from django.db import models

from .utils import camel_to_underscore


class SortActiveMixin(models.Model):
    """Adds Sort and Active columns

    Attributes:
        sort (integer, indexed)
        active (boolean, indexed)
    """
    class Meta:
        abstract = True

    sort = models.IntegerField(default=0,
                               db_default="0",
                               db_index=True)
    active = models.BooleanField(default=True,
                                 db_default="True",
                                 db_index=True)


class DefinitionMixin(SortActiveMixin):
    """Common properties for models that define entity concept

    Attributes:
        See SortActiveMixin
        name (string, not unique, required, indexed)
        short_description (string): Word or two about object
        long_description (string): Long description of object
        schema_name (string): Underscore/lower-case class name
    """
    class Meta:
        abstract = True
    #TODO problem with unique name and element option values
    name = models.CharField(max_length=25,
                            default="",
                            unique=False,
                            null=False,
                            db_index=True,
                            blank=False)
    short_definition = models.CharField(max_length=25, null=True, blank=True)
    long_definition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "<{class_name}(Name={instance_name})>".format(
            class_name=self.__class__.__name__,
            instance_name=self.name
        )

    @property
    def schema_name(self):
        return camel_to_underscore(self.name)