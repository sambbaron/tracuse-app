from model_mommy import mommy


class TestDataWindowuse(object):
    def __init__(self):
        # Users
        self.user1 = mommy.make("auth.User",
                                username="TestUser1"
                                )

        # Windowuse Objects
        self.windowuse_object1 = mommy.make("windowuse.WindowuseObject",
                                            title="Windowuse 1 Title",
                                            user=self.user1
                                            )
        self.windowuse_object2 = mommy.make("windowuse.WindowuseObject",
                                            title="Windowuse 2 Title",
                                            user=self.user1
                                            )

        # Viewuse Objects
        self.viewuse_object1 = mommy.make("viewuse.ViewuseObject",
                                          title="Viewuse 1 Title",
                                          user=self.user1,
                                          )
        self.viewuse_object2 = mommy.make("viewuse.ViewuseObject",
                                          title="Viewuse 2 Title",
                                          user=self.user1
                                          )

        # Windowuse-Viewuse Objects
        self.windowuse_viewuse1 = mommy.make("windowuse.WindowuseViewuse",
                                             windowuse_object=self.windowuse_object1,
                                             viewuse_object=self.viewuse_object1
                                             )
        self.windowuse_viewuse2 = mommy.make("windowuse.WindowuseViewuse",
                                             windowuse_object=self.windowuse_object1,
                                             viewuse_object=self.viewuse_object2
                                             )
