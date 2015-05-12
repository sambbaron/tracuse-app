from model_mommy import mommy


class TestDataAssociation(object):
    def __init__(self):
        # Datum Type
        self.datum_type1 = mommy.make("datum.DatumType",
                                      entity_name="TestDatumType1",
                                      repr_expression="{{name}}"
                                      )
        # Datum Objects
        self.datum_object1 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object2 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object3 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object4 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object5 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object6 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)
        self.datum_object7 = mommy.make("datum.DatumObject", datum_type=self.datum_type1)

        # Element Type for Name Identification
        self.element_data_type1 = mommy.make("element_type.ElementDataType",
                                             entity_name="String"
                                             )
        self.element_type1 = mommy.make("element_type.ElementType",
                                        entity_name="Name",
                                        element_data_type=self.element_data_type1
                                        )

        # Element Types to Datum Objects
        self.element_type_datum_object1 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object1,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object2 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object2,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object3 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object3,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object4 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object4,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object5 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object5,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object6 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object6,
                                                     element_type=self.element_type1
                                                     )
        self.element_type_datum_object7 = mommy.make("element_type.ElementTypeDatumObject",
                                                     datum_object=self.datum_object7,
                                                     element_type=self.element_type1
                                                     )

        # Element Value objects
        self.element_value_string1 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object1,
                                                element_value="Test Object1")
        self.element_value_string2 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object2,
                                                element_value="Test Object2")
        self.element_value_string3 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object3,
                                                element_value="Test Object3")
        self.element_value_string4 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object4,
                                                element_value="Test Object4")
        self.element_value_string5 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object5,
                                                element_value="Test Object5")
        self.element_value_string6 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object6,
                                                element_value="Test Object6")
        self.element_value_string7 = mommy.make("element_value.ElementValueString",
                                                element_type_datum_object=self.element_type_datum_object7,
                                                element_value="Test Object7")

        # Association Type
        self.association_type1 = mommy.make("association.AssociationType",
                                            entity_name="DefaultAssociationType"
                                            )

        # Association Directions
        self.association_direction1 = mommy.make("association.AssociationDirection",
                                                 association_direction_id=-1,
                                                 entity_name="parent"
                                                 )
        self.association_direction2 = mommy.make("association.AssociationDirection",
                                                 association_direction_id=0,
                                                 entity_name="both"
                                                 )
        self.association_direction3 = mommy.make("association.AssociationDirection",
                                                 association_direction_id=1,
                                                 entity_name="child"
                                                 )

        # Adjacent Associations
        self.adjacent_association1 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object1,
                                                child_datum=self.datum_object2,
                                                association_type=self.association_type1
                                                )
        self.adjacent_association2 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object2,
                                                child_datum=self.datum_object3,
                                                association_type=self.association_type1
                                                )
        self.adjacent_association3 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object3,
                                                child_datum=self.datum_object4,
                                                association_type=self.association_type1
                                                )
        self.adjacent_association4 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object1,
                                                child_datum=self.datum_object5,
                                                association_type=self.association_type1
                                                )
        self.adjacent_association5 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object1,
                                                child_datum=self.datum_object6,
                                                association_type=self.association_type1
                                                )
        self.adjacent_association6 = mommy.make("association.AssociationAdjacent",
                                                parent_datum=self.datum_object6,
                                                child_datum=self.datum_object7,
                                                association_type=self.association_type1
                                                )