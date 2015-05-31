import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import FilterSet
from .utils import run_filter_from_dict


class RunFilter(object):
    """Return list of filtered datums"""

    @staticmethod
    @login_required
    def filter_from_json(request):
        request_data = request.body.decode()
        serialized_data = json.loads(request_data)

        filter_response = run_filter_from_dict(**serialized_data)
        response = JsonResponse(list(filter_response), status=200, safe=False)

        return response

    @staticmethod
    @login_required
    def filter_from_set(request, pk):
        try:
            filter_set = FilterSet.objects.get(pk=pk)
        except FilterSet.DoesNotExist:
            raise Http404("Filter Set does not exist.")

        filter_response = filter_set.run_filter()
        response = JsonResponse(list(filter_response), status=200, safe=False)

        return response
