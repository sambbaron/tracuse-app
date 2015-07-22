from model_mommy import mommy


class TestDataUiObject(object):
    def __init__(self):
        # Users
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Ui Arrangement Type
        self.ui_arrangement_type1 = mommy.make("ui_object.UiArrangementType",
                                               entity_name="ArrangementType1",
                                               )
        self.ui_arrangement_type2 = mommy.make("ui_object.UiArrangementType",
                                               entity_name="ArrangementType2",
                                               )

        # Ui Formatting Type
        self.ui_formatting_type1 = mommy.make("ui_object.UiFormattingType",
                                              entity_name="FormattingType1",
                                              )
        self.ui_formatting_type2 = mommy.make("ui_object.UiFormattingType",
                                              entity_name="FormattingType2",
                                              )
