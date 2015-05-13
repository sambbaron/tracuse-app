from datetime import datetime

from model_mommy import mommy


class TestDataElementValue(object):
    def __init__(self):
        # Users
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Datum Groups
        self.group_area = mommy.make("datum.DatumGroup",
                                     entity_name="Area",
                                       sort=10)
        self.group_activity = mommy.make("datum.DatumGroup",
                                         entity_name="Activity",
                                       sort=20)
        self.group_time = mommy.make("datum.DatumGroup",
                                     entity_name="Time",
                                       sort=30)

        # Datum Types
        self.type_category = mommy.make("datum.DatumType",
                                        entity_name="Category",
                                        datum_group=self.group_area,
                                      str_expression="{{name}}",
                                      sort=10100)
        self.type_person = mommy.make("datum.DatumType",
                                      entity_name="Person",
                                      datum_group=self.group_area,
                                      str_expression="{{name}}")
        self.type_action = mommy.make("datum.DatumType",
                                      entity_name="Action",
                                      datum_group=self.group_activity,
                                      str_expression="{{name}}")
        self.type_event = mommy.make("datum.DatumType",
                                     entity_name="Event",
                                     datum_group=self.group_time,
                                     str_expression="{{name}}")

        # Datum Object
        self.datum_category = mommy.make("datum.DatumObject",
                                         datum_type=self.type_category)
        self.datum_person = mommy.make("datum.DatumObject",
                                       datum_type=self.type_person)
        self.datum_action = mommy.make("datum.DatumObject",
                                       datum_type=self.type_action)
        self.datum_event = mommy.make("datum.DatumObject",
                                      datum_type=self.type_event)


        # Element Data Types
        self.data_type_string = mommy.make("element_type.ElementDataType",
                                             entity_name="String"
                                             )
        self.data_type_datetime = mommy.make("element_type.ElementDataType",
                                             entity_name="Datetime"
                                             )

        # Element Types
        self.element_type_name = mommy.make("element_type.ElementType",
                                        entity_name="Name",
                                        element_data_type=self.data_type_string,
                                        str_expression=""
                                        )
        self.element_type_desc = mommy.make("element_type.ElementType",
                                        entity_name="Description",
                                        element_data_type=self.data_type_string,
                                        str_expression=""
                                        )
        self.element_type_firstname = mommy.make("element_type.ElementType",
                                                 entity_name="FirstName",
                                                 element_data_type=self.data_type_string,
                                                 str_expression=""
                                                 )
        self.element_type_lastname = mommy.make("element_type.ElementType",
                                                entity_name="LastName",
                                                element_data_type=self.data_type_string,
                                                str_expression=""
                                                )
        self.element_type_endingdate = mommy.make("element_type.ElementType",
                                                  entity_name="EndingDate",
                                                  element_data_type=self.data_type_datetime,
                                                  str_expression=
                                                  "Test datetime is {{ value|date:'F j, Y g:i A'}}"
                                                  )

        # Element Type - Datum Type
        self.element_category_name = mommy.make("element_type.ElementDatumType",
                                              make_m2m=True,
                                              datum_type=self.type_category,
                                              element_type=self.element_type_name
                                              )
        self.element_category_desc = mommy.make("element_type.ElementDatumType",
                                              make_m2m=True,
                                              datum_type=self.type_category,
                                              element_type=self.element_type_desc
                                              )
        self.element_event_endingdate = mommy.make("element_type.ElementDatumType",
                                                   make_m2m=True,
                                                   datum_type=self.type_event,
                                                   element_type=self.element_type_endingdate
                                                   )


        # Element Type - Datum Object
        self.object_category_name = mommy.make("element_type.ElementDatumObject",
                                                make_m2m=True,
                                                datum_object=self.datum_category,
                                                element_type=self.element_type_name
                                                )
        self.object_category_desc = mommy.make("element_type.ElementDatumObject",
                                               make_m2m=True,
                                               datum_object=self.datum_category,
                                               element_type=self.element_type_desc
                                               )
        self.object_event_endingdate = mommy.make("element_type.ElementDatumObject",
                                                  make_m2m=True,
                                                  datum_object=self.datum_event,
                                                  element_type=self.element_type_endingdate
                                                  )

        # Element Values
        self.value_category_name = \
            mommy.make("element_value.ElementValueString",
                       element_datum_object=self.object_category_name,
                       element_value="Test Object Name")
        self.value_event_endingdate = \
            mommy.make("element_value.ElementValueDatetime",
                       element_datum_object=self.object_event_endingdate,
                       element_value=datetime(2015, 5, 12, 16, 30))
