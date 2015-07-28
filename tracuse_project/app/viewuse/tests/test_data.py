from model_mommy import mommy


class TestDataViewuse(object):
    def __init__(self):
        # Users
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Viewuse Arrangement
        self.viewuse_arrangement1 = mommy.make("viewuse.ViewuseArrangement",
                                          entity_name="ViewuseArrangement1"
                                          )

        # Viewuse Object
        self.viewuse_object1 = mommy.make("viewuse.ViewuseObject",
                                          title="Viewuse 1 Title",
                                          viewuse_arrangement = self.viewuse_arrangement1,
                                          datum_filter='{"TestFilter1": "TestFilter1"}',
                                          user=self.user1
                                          )
        self.viewuse_object2 = mommy.make("viewuse.ViewuseObject",
                                          title="Viewuse 2 Title",
                                          viewuse_arrangement = self.viewuse_arrangement1,
                                          datum_filter='{"TestFilter2": "TestFilter2"}',
                                          )
