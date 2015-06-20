import json

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum)
from utils.serializer import serialize_all


class ViewuseObjectSerializer(ViewuseObject):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        output["filter_json"] = json.loads(output["filter_json"])
        return output

    ViewuseObject.serial_basic = serial_basic

    def serial_related(self):
        """All properties with relations
        """
        output = self.serial_basic()
        output["viewuse_arrangement"] = self.viewuse_arrangement_id
        output["viewuse_datum"] = self.viewuse_datum_id
        return output

    ViewuseObject.serial_related = serial_related


class ViewuseArrangementSerializer(ViewuseArrangement):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    ViewuseArrangement.serial_basic = serial_basic


class ViewuseDatumSerializer(ViewuseDatum):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    ViewuseDatum.serial_basic = serial_basic
