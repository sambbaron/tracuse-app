from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.app_index, name='app_home'),

]

