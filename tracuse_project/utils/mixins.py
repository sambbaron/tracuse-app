from django.db import models

from utils.names import camel_to_underscore, camel_to_spaced_capital


class BaseMixin(models.Model):
    """Adds default column set

    Attributes:
        sort (integer, indexed)
        active (boolean, indexed)
        created (datetime): Timestamp at row insertion
        modified (datetime): Timestamp at row update

    Methods:
        last_sorted
    """

    class Meta:
        abstract = True
        ordering = ["sort"]

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

    @classmethod
    def last_sorted(cls):
        """Object with maximum sort value
        Used in _calc_sort methods
        """
        return cls.objects.order_by("-sort")[0]


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
        readable_plural_name (string, calculated):
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
    readable_name = models.CharField(max_length=25,
                                     default="",
                                     null=False, blank=False,
                                     unique=False, db_index=True
                                     )
    schema_name = models.CharField(max_length=25,
                                   default="",
                                   null=False, blank=False,
                                   unique=False
                                   )
    readable_plural_name = models.CharField(max_length=25,
                                            default="",
                                            null=False, blank=False,
                                            unique=False
                                            )
    short_definition = models.CharField(max_length=25,
                                        null=True, blank=True
                                        )
    long_definition = models.CharField(max_length=100,
                                       null=True, blank=True
                                       )

    def __str__(self):
        return self.readable_name

    def _set_readable_name(self):
        if self.readable_name is "":
            self.readable_name = camel_to_spaced_capital(self.entity_name)

    def _set_schema_name(self):
        if self.schema_name is "":
            self.schema_name = camel_to_underscore(self.entity_name)

    def _set_readable_plural_name(self):
        if self.readable_plural_name is "":
            readable_name = self.readable_name
            if readable_name and readable_name[-1] is "s":
                output = readable_name + "es"
            else:
                output = readable_name + "s"
            self.readable_plural_name = output

    def save(self, *args, **kwargs):
        self._set_readable_name()
        self._set_schema_name()
        self._set_readable_plural_name()
        super(EntityMixin, self).save(*args, **kwargs)