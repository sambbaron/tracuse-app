
from django.core.management.base import BaseCommand

try:
    from datum.models import DatumGroup, DatumType
except ImportError:
    from ....datum.models import DatumGroup, DatumType



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(">>>>>>>>>>Sandbox Begin<<<<<<<<<<")

        # DatumGroup._meta.get_field

        self.stdout.write(">>>>>>>>>>Sandbox End<<<<<<<<<<")