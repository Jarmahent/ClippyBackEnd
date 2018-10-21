from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('', views.CopyDataView, name="copydata"),
]

urlpatterns = format_suffix_patterns(urlpatterns)