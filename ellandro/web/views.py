from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView
from .models import Client
from .forms import ClientForm
from django.urls import reverse_lazy
# Create your views here.

class Homepage(ListView):
    model = Client 
    template_name = 'homepage.html'

class Products(CreateView):
    model = Client
    template_name = 'products.html'
    #form_class = ClientForm 
    fields = '__all__'


class Contact(CreateView):
    model = Client
    template_name = 'form.html'
    form_class = ClientForm 
    success_url = reverse_lazy('homepage')

class ContactPage(ListView):
    model = Client 
    template_name = 'contact.html'

