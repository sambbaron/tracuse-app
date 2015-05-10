import json

from django.http import HttpResponse

from components.datum.models import DatumObject

def index(request):

    datum = DatumObject.objects.first()
    datum_dict = datum.as_dict_all
    datum_json = json.dumps(datum_dict)
    response = HttpResponse(datum_json)
    return response

