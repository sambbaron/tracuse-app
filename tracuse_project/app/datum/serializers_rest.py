from rest_framework import serializers

from .models import DatumGroup, DatumObject
from app.association.models import AssociationAll

class AssociationChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssociationAll
        fields = ('child_datum', 'distance')

class DatumGroupMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatumGroup


class DatumObjectMainSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    datum_group = serializers.ReadOnlyField(source="datum_group.datum_group_id")

    class Meta:
        model = DatumObject
        fields = ('datum_object_id', 'datum_group', 'datum_type', 'active', 'sort', 'user',
                  'element_types', 'adjacent_child_datums', 'all_child_datums')


