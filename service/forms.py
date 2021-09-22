from django import forms
from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'firstName': forms.TextInput(attrs={'class':'validate'}),
            'lastName': forms.TextInput(attrs={'class':'validate'}),
            'phoneNumber':forms.TextInput(attrs={'class':'validate'}),
            'email':forms.EmailInput(attrs={'class':'validate'}),
            'subject':forms.TextInput(attrs={'class':'validate'}),
            'problemDescription':forms.TextInput(attrs={'class':'materialize-textarea'}),

        }
