
from datetime import datetime

from django.db import models

from .utils import camel_to_underscore, camel_to_spaced_lower, camel_to_spaced_capital


class BaseMixin(models.Model):
    """Adds default column set

    Attributes:
        sort (integer, indexed)
        active (boolean, indexed)
        created (datetime): Timestamp at row insertion
        modified (datetime): Timestamp at row update
    """

    class Meta:
        abstract = True

    sort = models.IntegerField(default=0,
                               db_index=True
                               )
    active = models.BooleanField(default=True,
                                 db_index=True
                                 )
    # TODO Add columns when schema is more stable
    # FIXME Django Limitation - Can't do DEFAULT SQL statement
    # created = models.DateTimeField(default=datetime.now)
    # modified = models.DateTimeField(auto_now=True)


class EntityMixin(BaseMixin):
    """Common properties for models that define an entity

    Attributes:
        See BaseMixin
        entity_name (string, required, unique, indexed):
            CamelCase entity name --> ItemStatus
            Used for class mapping
        schema_name (string, calculated):
            lower case, underscored entity name --> item_status
            Used for table mapping
        common_name (string, calculated):
            lower case, spaced entity name --> item status
            Used for datum associations
        plural_name (string, calculated):
            common name, pluralized --> item statuses
        short_description (string): Word or two about object
        long_description (string): Long description of object
        schema_name (string): Underscore/lower-case class name
    """

    class Meta:
        abstract = True

    # TODO problem with unique name and element option values
    entity_name = models.CharField(max_length=25,
                                   default="",
                                   null=False, blank=False,
                                   unique=False, db_index=True
                                   )
    short_definition = models.CharField(max_length=25,
                                        null=True, blank=True
                                        )
    long_definition = models.CharField(max_length=100,
                                       null=True, blank=True
                                       )

    @property
    def schema_name(self):
        return camel_to_underscore(self.entity_name)

    @property
    def common_name(self):
        return camel_to_spaced_lower(self.entity_name)

    @property
    def plural_name(self):
        output = ""
        spaced_lower = camel_to_spaced_lower(self.entity_name)
        if spaced_lower[-1] is "s":
            output = spaced_lower + "es"
        else:
            output = spaced_lower + "s"
        return output

    def __str__(self):
        return "<{class_name}(Name={instance_name})>".format(
            class_name=self.__class__.__name__,
            instance_name=camel_to_spaced_capital(self.entity_name)
        )