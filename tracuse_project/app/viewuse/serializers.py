import json

from .models import (ViewuseObject,
                     ViewuseArrangement,
                     ViewuseDatum)

from app.common.serializers import serialize_all


class ViewuseObjectSerializer(ViewuseObject):
    class Meta:
        abstract = True

    def serial_basic(self):
        """All properties"""
        output = serialize_all(self.__class__, self)
        return output

    ViewuseObject.serial_basic = serial_basic

    def serial_for_ui(self):
        """Properties for rendering ui"""
        filter_list = []
        for filter in self.viewuse_filters.all():
            filter_list.append(json.loads(filter.filter_json))
        output = serialize_all(self.__class__, self)
        output["arrangement"] = self.viewuse_arrangement.schema_name
        output["datum"] = self.viewuse_datum.schema_name
        output["filters"] = filter_list
        return output

    ViewuseObject.serial_basic = serial_basic


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
