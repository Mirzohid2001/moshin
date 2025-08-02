from django.shortcuts import render
from django.views.generic import ListView
from .models import Partner, Partnership

# Create your views here.

class PartnerListView(ListView):
    """Список партнеров"""
    model = Partner
    template_name = 'partners/partner_list.html'
    context_object_name = 'partners'
    
    def get_queryset(self):
        return Partner.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partnerships'] = Partnership.objects.filter(is_active=True)
        return context
