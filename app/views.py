from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Contact


def create_contact(request):
    name = request.POST.get('contactname')
    phone_number = request.POST.get('phone_number')
    contact = Contact.objects.create(name=name, phone_number=phone_number)
    contacts = Contact.objects.all()

    return render(request, 'contact-list.html', {'contacts': contacts})


def delete_contact(request, pk):
    contact_id = Contact.objects.get(id=pk)
    contact_id.delete()
    contacts = Contact.objects.all()
    return render(request, 'contact-list.html', {'contacts': contacts})


class ContactList(ListView):
    template_name = 'contact.html'
    model = Contact
    context_object_name = 'contacts'