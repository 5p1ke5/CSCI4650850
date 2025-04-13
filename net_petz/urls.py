from django.urls import path
from . import views
app_name = 'pets'

urlpatterns = [
    path('', views.net_petz_list, name="list"),
    path('<slug:slug>', views.net_petz_page, name="page"),
]
