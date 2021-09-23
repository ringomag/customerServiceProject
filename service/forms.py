from django import forms
from django.forms import ModelForm
from .models import Customer, Comment
from datetime import datetime

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ('firstName', 'lastName', 'phoneNumber', 'email', 'subject', 'problemDescription', 'dateTimeCallback')

        widgets = {
            'firstName': forms.TextInput(attrs={'class':'validate'}),
            'lastName': forms.TextInput(attrs={'class':'validate'}),
            'phoneNumber':forms.TextInput(attrs={'class':'validate'}),
            'email':forms.EmailInput(attrs={'class':'validate'}),
            'subject':forms.TextInput(attrs={'class':'validate'}),
            'problemDescription':forms.TextInput(attrs={'class':'materialize-textarea'}),
            'dateTimeCallback':forms.DateTimeInput(attrs={'id':"datetimepicker"}),

        }
    def clean(self):
            cleaned_data = super().clean()
            datum = datetime.strptime(self.data['dateTimeCallback'], "%Y/%m/%d %H:%M")
            
            cleaned_data['dateTimeCallback'] = datetime.strftime(datum, "%Y-%m-%d %H:%M")
            return cleaned_data

    def full_clean(self):
            cleaned_data = super().full_clean()
            if 'dateTimeCallback' in self.errors:
                del self.errors['dateTimeCallback']
            return cleaned_data

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'comment', 'customer', )

        widgets = {
            'user': forms.Select(attrs={'class':'browser-default'}),
            'customer': forms.Select(attrs={'class':'browser-default'}),
            'comment': forms.TextInput(attrs={'class':'validate'}),

        }