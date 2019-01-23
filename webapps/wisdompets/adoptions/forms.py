from django import forms
from datetime import datetime
from .models import Pet


class SearchForm(forms.Form):
    q = forms.CharField()
    pet_sex = forms.BooleanField()
    pet_email = forms.EmailField()
    pet_species = forms.ChoiceField(choices=(('dog', 'Dogs'), ('cat', 'Cats'),
                                             ('bird', 'Birds'), ('lizard', 'Lizards')))
    pet_submit_date = forms.DateField()


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'sex', 'age', 'description', 'submitter',
                  'vaccination']
