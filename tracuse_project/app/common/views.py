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
