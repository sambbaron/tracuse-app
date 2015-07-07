from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from app.common.models import EntityModel, BaseModel


class TracuserLanding(BaseModel):
    """Users captured from website landing sign-up form

    Attributes:
        See BaseModel
        name (string)
        email (string)
        comments (large text)
    """

    class Meta(EntityModel.Meta):
        db_table = "tracuser_landing"
        verbose_name = "User Landing Signup"

    tracuser_landing_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)