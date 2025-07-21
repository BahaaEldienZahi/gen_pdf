# forms.py
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=200)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15, required=False)
    company = forms.CharField(max_length=100, required=False)
    address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    message = forms.CharField(widget=forms.Textarea)
    terms = forms.BooleanField(required=True, label="I agree to the terms and conditions")