from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.datum.models import (DatumGroup,
                              DatumType,
                              DatumObject)
from app.element_type.models import (ElementOption,
                                     ElementDatumObject)

@login_required
def app_index(request):
    return render(request, "app/base_app.html")



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

    element_options = ElementOption.objects.all()
    response_dict["element_options"] = element_options

    return render(request, "tester/datums.html", response_dict)


def datums_update(request, datum_pk):
    data = request.POST

    for dict_key in data.keys():

        if dict_key != "csrfmiddlewaretoken":

            element_datum_object = \
                ElementDatumObject.objects.filter(pk=int(dict_key)).first()

            if element_datum_object:
                element_value_object = element_datum_object.element_value
                element_value_object.elvalue = data[dict_key]
                element_value_object.save()

    return HttpResponseRedirect("/app/tester")


def datums_delete(request, datum_pk):
    data = request.POST

    datum_pk = int(data["datum-pk"])

    datum = DatumObject.objects.filter(pk=datum_pk).all()

    if datum:
        datum[0].delete()

    return HttpResponseRedirect("/app/tester")


def datums_create(request):
    data = request.POST

    datum_type_pk = int(data["create-datum-type"])

    datum = DatumObject.objects.create(user_id=1,
                                       datum_type_id=datum_type_pk
                                       )

    return HttpResponseRedirect("/app/tester")