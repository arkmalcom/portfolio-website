from django import forms

TOPICS = [
    ("DATA", "Data Science/Data Analysis"),
    ("WEBFRONT", "Front-end Work"),
    ("WEBBACK", "Back-end Work"),
]

class ContactForm(forms.Form):
    topic = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-select'}), choices=TOPICS)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=200)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), max_length=200)
    message = forms.CharField(widget = forms.Textarea(attrs={'class': 'form-control'}), max_length=2000)
