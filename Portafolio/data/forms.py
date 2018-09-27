from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['firstname','lastname']


    """firstname = forms.CharField(label='Name:',required=True)
    lastname = forms.CharField(label='LastName:',required=True)"""

class ProjectForm(forms.Form):
    title = forms.CharField(label='Title:', required=True, widget=forms.TextInput(
        attrs={'class':'border-radius', 'placeholder':'Title of your project'}
    ))
    description = forms.CharField(label='Description:', required=True, widget=forms.Textarea(
        attrs={'class':'border-radius', 'placeholder':'Description of your project', 'rows': 3}
    ), min_length=10, max_length=120)
    image = forms.ImageField(label='Image:', required=True)
    link = forms.URLField(label='URL:', required=True, widget=forms.URLInput(
        attrs={'class':'border-radius', 'placeholder':'URL of your project'}
    ))