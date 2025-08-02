from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.PartnerListView.as_view(), name='partner_list'),
] 