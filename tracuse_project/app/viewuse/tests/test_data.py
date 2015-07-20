from model_mommy import mommy


class TestDataViewuse(object):
    def __init__(self):
        # Users
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Viewuse Arrangements
        self.viewuse_arrangement1 = mommy.make("viewuse.ViewuseArrangement",
                                               entity_name="Arrangement1",
                                               )

        # Viewuse Datums
        self.viewuse_datum1 = mommy.make("viewuse.ViewuseDatum",
                                         entity_name="Datum1",
                                         )
        self.viewuse_datum2 = mommy.make("viewuse.ViewuseDatum",
                                         entity_name="Datum2",
                                         )

        # Viewuse Object
        self.viewuse_object1 = mommy.make("viewuse.ViewuseObject",
                                          title="Viewuse 1 Title",
                                          viewuse_arrangement=self.viewuse_arrangement1,
                                          viewuse_datum=self.viewuse_datum2,
                                          datum_filter='{"TestFilter1": "TestFilter1"}',
                                          user=self.user1
                                          )
        self.viewuse_object2 = mommy.make("viewuse.ViewuseObject",
                                          title="Viewuse 2 Title",
                                          viewuse_arrangement=self.viewuse_arrangement1,
                                          viewuse_datum=self.viewuse_datum1,
                                          datum_filter='{"TestFilter2": "TestFilter2"}',
                                          )

        # Nested Viewuses
        self.viewuse_nested1 = mommy.make("viewuse.ViewuseNested",
                                          parent_viewuse=self.viewuse_object1,
                                          nested_viewuse=self.viewuse_object2
                                          )
