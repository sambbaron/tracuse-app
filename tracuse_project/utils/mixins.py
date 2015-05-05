from django.db import models

from utils.names import camel_to_underscore, camel_to_spaced_capital


class BaseMixin(models.Model):
    """Adds default column set

    Attributes:
        active (boolean, indexed)
        sort (integer, indexed)
        sort_base_length (integer, default=3):
            number of digits in base sort value
        sort_parts (list of model properties):
            sort_values from parent objects
            ordering matters to build sort value
        created (datetime): Timestamp at row insertion
        modified (datetime): Timestamp at row update

    Methods:
        last_sort_value: last object by sort value
        _calc_sort: calculate sort value
    """

    class Meta:
        abstract = True
        ordering = ["sort"]

    active = models.BooleanField(default=True,
                                 db_index=True
                                 )
    sort = models.BigIntegerField(default=0,
                                  db_index=True
                                  )
    sort_base_length = 3
    sort_parts = []

    # TODO Add columns when schema is more stable
    # FIXME Django Limitation - Can't do DEFAULT SQL statement
    # created = models.DateTimeField(default=datetime.now)
    # modified = models.DateTimeField(auto_now=True)

    def last_sort_value(self):
        """Object with maximum sort value
        Exclusive of current object
        Used in _calc_sort methods
        """
        max_value = self.__class__.objects.exclude(pk=self.pk).aggregate(models.Max("sort"))
        if max_value["sort__max"] is None:
            return 0
        else:
            return max_value["sort__max"]

    def _calc_sort(self, after_object=None, sort_base_length=0, increment=1, sort_prefix_parts=[]):
        """Calculate sort value

        Arguments:
            after_object (object):
                if none, add to end
            sort_base_length (integer):
                number of digits to append to sort value
                if -1, then no base sort, only sort prefix
            increment (integer):
                add value to after_object sort
            sort_prefix_parts (list of model properties, default=self.sort_parts):
                sort_values from parent objects
                ordering matters to build sort value

        Return:
            sort value (integer)
        """

        sort_prefix = ""
        for sort_part in sort_prefix_parts:
            sort_prefix += str(sort_part)

        new_sort_suffix = ""
        if sort_base_length != -1:

            if after_object:
                after_sort = str(after_object.sort)
            else:
                after_sort = str(self.last_sort_value())
            after_sort_value = int(after_sort[-sort_base_length:])

            if after_sort_value == 0:
                # No records in table - create first sort value
                new_sort_value = 10 ** (sort_base_length - 1)
            else:
                new_sort_value = int(after_sort_value) + increment
            new_sort_suffix = str(new_sort_value)

        new_sort = sort_prefix + new_sort_suffix

        return int(new_sort)

    def _get_sort_value(self, **kwargs):
        sort_value = self._calc_sort(sort_base_length=self.sort_base_length,
                                     sort_prefix_parts=self.sort_parts
                                     )
        return sort_value

    def save(self, *args, **kwargs):
        if self.sort == 0:
            self.sort = self._get_sort_value()

        super().save(*args, **kwargs)


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

    Methods:
        set_readable_name
        set_schema_name
        set_readable_plural_name
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

    def _get_readable_name(self):
        return camel_to_spaced_capital(self.entity_name)

    def _get_schema_name(self):
        return camel_to_underscore(self.entity_name)

    def _get_readable_plural_name(self):
        readable_name = self.readable_name
        if readable_name and readable_name[-1] is "s":
            output = readable_name + "es"
        else:
            output = readable_name + "s"
        return output

    def set_readable_name(self):
        self.readable_name = self._get_readable_name()

    def set_schema_name(self):
        self.schema_name = self._get_schema_name()

    def set_readable_plural_name(self):
        self.readable_plural_name = self._get_readable_plural_name()

    def save(self, *args, **kwargs):
        if self.readable_name is "":
            self.set_readable_name()

        if self.schema_name is "":
            self.set_schema_name()

        if self.readable_plural_name is "":
            self.set_readable_plural_name()

        super().save(*args, **kwargs)