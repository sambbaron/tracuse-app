from django.conf.urls import url

from . import api
from . import views

urlpatterns = [

    # App Home
    url(r'^$', views.app_index, name='app_home'),

    # New API
    url(r'^datum_groups/$', api.datum_groups_get),
    url(r'^datum_types/$', api.datum_types_get),
    url(r'^datum_objects/$', api.datum_objects_get),

]

