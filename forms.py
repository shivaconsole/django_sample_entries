from django import forms
from .models import *


class EnquiryForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}))
    class Meta:
        model = Enquiry
        fields = ('enquiry_type', 'name', 'email', 'mobile_number', 'notes')


class EnquiryTypeForm(forms.ModelForm):
    class Meta:
        model = EnquiryType
        fields = '__all__'
