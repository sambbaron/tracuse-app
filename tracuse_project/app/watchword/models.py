from django.db import models

from app.common.models import BaseModel


class WatchwordModel(BaseModel):
    """Common columns for Watchword models

    Keywords used to trigger object filtering
        and automatic associations

    Attributes:
        See BaseModel
        watchword (string, required):
            words or phrase to assign objects
        filter_test_scope (integer, fk, optional):
            FilterSet used to limit scope of watchword test
            If null, then watchword is tested against all objects
    """

    class Meta(BaseModel.Meta):
        abstract = True
        default_related_name = "watchwords"

    watchword = models.CharField(max_length=100,
                                 null=False, blank=False
                                 )
    filter_test_scope = models.ForeignKey("filter.FilterSet",
                                          db_column="filter_set_id",
                                          null=True, blank=True
                                          )


class WatchwordDatumType(WatchwordModel):
    """Datum Type Watchwords

    Attributes:
        See WatchwordModel (see BaseModel)
        datum_type_id (integer, fk, required):
            DatumType
    """

    class Meta(BaseModel.Meta):
        db_table = "watchword_datum_type"
        verbose_name = "Datum Type Watchword"

    watchword_datum_type_id = models.AutoField(primary_key=True)
    datum_type = models.ForeignKey("datum.DatumType",
                                   db_column="datum_type_id",
                                   null=False, blank=False
                                   )


class WatchwordDatumObject(WatchwordModel):
    """Datum Element Value Watchwords

    Attributes:
        See WatchwordModel (see BaseModel)
        datum_object_id (integer, fk, required):
            DatumObject
    """

    class Meta(BaseModel.Meta):
        db_table = "watchword_datum_object"
        verbose_name = "Datum Object Watchword"

    watchword_datum_object_id = models.AutoField(primary_key=True)
    datum_object = models.ForeignKey("datum.DatumObject",
                                     db_column="datum_object_id",
                                     null=False, blank=False
                                     )


class WatchwordAssociationType(WatchwordModel):
    """Association Type Watchwords

    Attributes:
        See WatchwordModel (see BaseModel)
        association_type_id (integer, fk, required):
            AssociationType
    """

    class Meta(BaseModel.Meta):
        db_table = "watchword_association_type"
        verbose_name = "Association Type Watchword"

    watchword_association_type_id = models.AutoField(primary_key=True)
    association_type = models.ForeignKey("association.AssociationType",
                                         db_column="association_type_id",
                                         null=False, blank=False
                                         )