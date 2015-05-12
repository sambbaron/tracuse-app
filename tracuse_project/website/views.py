from django.shortcuts import render, HttpResponseRedirect

from app.datum.models import (DatumGroup,
                                     DatumType,
                                     DatumObject)
from app.element_type.models import ElementDatumObject


def datums_get(request):
    """Basic view for testing

    Add/remove/filter datums
    """
    response_dict = {}

    datum_groups = DatumGroup.objects.all()
    response_dict["datum_groups"] = datum_groups

    datum_types = DatumType.objects.all()
    response_dict["datum_types"] = datum_types

    datum_objects = DatumObject.objects.all()
    response_dict["datum_objects"] = datum_objects

    return render(request, "datums.html", response_dict)


def datums_post(request, datum_pk):
    data = request.POST

    for dict_key in data.keys():

        if dict_key != "csrfmiddlewaretoken":

            element_datum_object = \
                ElementDatumObject.objects.filter(pk=int(dict_key)).all()

            if element_datum_object:
                element_datum_object = element_datum_object[0]
                element_value_object = element_datum_object.element_value
                element_value_object.element_value = data[dict_key]
                element_value_object.save()

    return HttpResponseRedirect("/")


def datums_delete(request, datum_pk):
    data = request.POST

    datum_pk = int(data["datum-pk"])

    datum = DatumObject.objects.filter(pk=datum_pk).all()

    if datum:
        datum[0].delete()

    return HttpResponseRedirect("/")


def datums_add(request):
    data = request.POST

    datum_type_pk = int(data["add-datum-type"])

    datum = DatumObject.objects.create(user_id=1,
                                       datum_type_id=datum_type_pk
                                       )

    return HttpResponseRedirect("/")