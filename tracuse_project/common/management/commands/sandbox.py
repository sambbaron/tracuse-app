
from django.core.management.base import BaseCommand

from datum.models import DatumGroup, DatumType, DatumObject



class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(">>>>>>>>>>Sandbox Begin<<<<<<<<<<")

        new_datum = DatumObject()
        new_datum.datum_type = DatumType.objects.get(pk=1)
        new_datum.user_id = 1
        new_datum.save()
        print(new_datum)

        self.stdout.write(">>>>>>>>>>Sandbox End<<<<<<<<<<")