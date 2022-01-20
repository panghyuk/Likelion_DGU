from unicodedata import name
from django.urls import path
from .views import *

app_name='homework'
urlpatterns = [
  path('list/', showlist, name="showlist"),
  path('write/', writehw, name="writehw"),
  path('<int:assignment_id>/', showdetail, name="showdetail"),
]
