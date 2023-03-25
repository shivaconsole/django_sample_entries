from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from . import models
from . import forms
User = get_user_model()


class EnquiryCreateView(CreateView):
    template_name = 'enquiry/form.html'
    form_class = forms.EnquiryForm
    success_url = reverse_lazy('enquiry')

class EnquiryUpdateView(UpdateView):
    template_name = 'enquiry/form.html'
    model = models.Enquiry
    form_class = forms.EnquiryForm
    success_url = reverse_lazy('enquiry')

class EnquiryListView(ListView):
    template_name = 'enquiry/list.html'
    model = models.Enquiry
    paginate_by = 10

class EnquiryTypeCreateView(CreateView):
    template_name = 'enquiry_type/form.html'
    form_class = forms.EnquiryTypeForm
    success_url = reverse_lazy('enquiry_type')

class EnquiryTypeUpdateView(UpdateView):
    template_name = 'enquiry_type/form.html'
    model = models.EnquiryType
    form_class = forms.EnquiryTypeForm
    success_url = reverse_lazy('enquiry_type')

class EnquiryTypeListView(ListView):
    template_name = 'enquiry_type/list.html'
    model = models.EnquiryType
    paginate_by = 10
    
