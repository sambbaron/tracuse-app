from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from website import views

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="website/base_website.html"), name='index'),
    url(r'^learn/$', TemplateView.as_view(template_name="website/learn.html"), name='learn'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.common.urls')),
    url(r'^api/', include('app.common.api')),

]
