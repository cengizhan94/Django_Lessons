from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("cengo", views.cengo, name="cengo"),
    path("zeynep", views.zeynep, name="zeynep"),
    path("<str:name>",views.greet, name="greet"),
]