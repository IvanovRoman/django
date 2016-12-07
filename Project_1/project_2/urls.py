from django.conf.urls import url
from project_2 import views

urlpatterns = (
    url(r'^(?:(?P<cat_id>\d+)/)?$', views.index, name = "index"),
    url(r'^good/(?P<cat_id>\d+)/$', views.good, name = "good"),
    )