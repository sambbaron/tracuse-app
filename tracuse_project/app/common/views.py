from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def app_index(request):
    return render(request, "app/base_app.html")

