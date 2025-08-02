from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactInfo
from .forms import ContactForm

def contact(request):
    """Контактная страница"""
    contact_info = ContactInfo.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'contact_info': contact_info,
        'form': form,
    }
    return render(request, 'contact/contact.html', context)
