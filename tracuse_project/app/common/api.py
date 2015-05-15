import json

from django.shortcuts import HttpResponse

from app.datum.models import (DatumGroup,
                              DatumType,
                              DatumObject)
from app.element_type.models import (ElementOption,
                                     ElementDatumObject)


def datum_groups_get(request):
    datum_groups = DatumGroup.objects.values()
    json_data = json.dumps(list(datum_groups))
    response = HttpResponse(json_data)
    return response
