from django.urls import path
from home import views
from backend import views as bViews

urlpatterns = [
    path('', views.homePage, name="home"),
    path('api', bViews.CopyDataView, name="root")
]
