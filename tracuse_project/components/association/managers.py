from django.db import models


class AssociationQuerySet(models.QuerySet):

    def filter_distance(self, distance_limit=1):
        if distance_limit:
            distance_filter = models.Q(distance__lte=distance_limit)
            return self.filter(distance_filter)
        else:
            return self

    def exclude_self(self, exclude_self=False):
        if exclude_self:
            self_exclude = models.Q(parent_datum=models.F("child_datum"))
            return self.exclude(self_exclude)
        else:
            return self


class AssociationManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return AssociationQuerySet(self.model, using=self._db)

    def filter_distance(self):
        return self.get_queryset().filter_distance()

    def exclude_self(self):
        return self.get_queryset().exclude_self()
