from django.db import models

from app.common.utils.entity import (camel_to_underscore,
                                     camel_to_spaced_capital,
                                     sort_range_value)


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


    def _last_sort_value(self, sort_start=0, sort_end=0):
        """Object with maximum sort value
        Exclusive of current object
        Used in _calc_sort_value methods

        Arguments:
            sort_start (integer):
            sort_end (integer):
                used to lookup last sort value in sequence
        """
        max_value_objects = self.__class__.objects.exclude(pk=self.pk)
        if sort_end != 0:
            max_value_objects = max_value_objects.filter(sort__range=(sort_start, sort_end))

        max_value_query = max_value_objects.aggregate(models.Max("sort"))
        if max_value_query["sort__max"] is None:
            return 0
        else:
            return max_value_query["sort__max"]

    def _calc_sort_value(self, after_object=None, sort_base_length=0, increment=1, sort_prefix_parts=[]):
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

        new_sort_prefix = ""
        for sort_part in sort_prefix_parts:
            new_sort_prefix += str(sort_part)

        new_sort_suffix = ""
        if sort_base_length != -1:

            if after_object:
                after_sort_str = str(after_object.sort)
            else:
                sort_start = sort_range_value(sort_prefix=new_sort_prefix,
                                              sort_base_length=sort_base_length,
                                              return_start=True
                                              )
                sort_end = sort_range_value(sort_prefix=new_sort_prefix,
                                            sort_base_length=sort_base_length,
                                            return_start=False
                                            )
                after_sort_str = str(self._last_sort_value(sort_start, sort_end))

            after_sort_prefix = after_sort_str[:len(after_sort_str) - sort_base_length]
            after_sort_value = int(after_sort_str[-sort_base_length:])

            if after_sort_value == 0 or after_sort_prefix != new_sort_prefix:
                # Reset sort value
                new_sort_value = 10 ** (sort_base_length - 1)
            else:
                new_sort_value = int(after_sort_value) + increment
            new_sort_suffix = str(new_sort_value)

        new_sort = new_sort_prefix + new_sort_suffix

        return int(new_sort)

    def get_sort_value(self, **kwargs):
        """Return sort value based on model class defaults"""
        sort_value = self._calc_sort_value(sort_base_length=self.sort_base_length,
                                           sort_prefix_parts=self.sort_parts,
                                           **kwargs
                                           )
        return sort_value

    def save(self, *args, **kwargs):
        """Set calculated sort value if zero"""
        if self.sort == 0:
            self.sort = self.get_sort_value()

        super().save(*args, **kwargs)

    @classmethod
    def reset_sort(cls, increment=10):
        """Reset all sort values based on current sort order"""
        objects_sorted = cls.objects.order_by("sort").all()
        objects_sorted.update(sort=0)

        after_object = None
        for obj in objects_sorted:
            obj.sort = obj.get_sort_value(after_object=after_object,
                                          increment=increment
                                          )
            obj.save()
            after_object = obj


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
        schema_name (string): Underscore/lower-case class name
        short_definition (string): Word or two about object
        long_definition (string): Long description of object
        usage (string): How this object benefits the user
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
    usage = models.CharField(max_length=100,
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
        """Set entity names if empty"""

        if self.readable_name is "":
            self.set_readable_name()

        if self.schema_name is "":
            self.set_schema_name()

        if self.readable_plural_name is "":
            self.set_readable_plural_name()

        super().save(*args, **kwargs)