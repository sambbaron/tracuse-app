import os

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

from django.conf import settings


class Command(BaseCommand):
    help = ("Extended dumpdata command. "
            "Output the contents of a group of models as a fixture of the given format."
            "Input model group - replaces 'app_label.model_name'. "
            "Same arguments as built-in dumpdata.")

    def add_arguments(self, parser):
        parser.add_argument('model_group', metavar='model_group',
                            help='Model group defined in settings.MODEL_GROUPS.')

    def handle(self, *args, **options):

        model_group = options.get("model_group")

        # Use json as default file name
        if not options.get("format"):
            options["format"] = "json"

        # Set default output as fixtures directory/model name
        if not options.get("output"):
            fixture_path = settings.FIXTURE_DIRS[0]
            file_name = model_group + "." + options.get("format")
            file_path = os.path.join(fixture_path, file_name)
            options["output"] = file_path

        models = ()
        if model_group in settings.MODEL_GROUPS:
            models = settings.MODEL_GROUPS[model_group]
        else:
            raise CommandError("Unknown model group")

        call_command("dumpdata", *models, **options)
