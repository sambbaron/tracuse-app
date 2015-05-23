import json

from django.http import HttpResponse, JsonResponse, Http404
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from app.filter.utils import run_filter_from_dict

class RunFilter(object):
    """Return all datum_groups"""

    @staticmethod
    @login_required
    def run_filter_manual(request):
        request_data = request.body.decode()
        serialized_data = json.loads(request_data)

        filter_response = run_filter_from_dict(**serialized_data)
        response = JsonResponse(list(filter_response), status=200, safe=False)

        return response
