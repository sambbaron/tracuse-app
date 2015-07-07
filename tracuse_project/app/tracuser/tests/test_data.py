from model_mommy import mommy


class TestDataTracuser(object):
    def __init__(self):
        # Users
        self.landing1 = mommy.make("tracuser.TracuserLanding",
                                   name="TestUser1",
                                   email="test@test.com",
                                   comments="I am a test user"
                                   )
