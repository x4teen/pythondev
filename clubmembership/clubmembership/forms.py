from django.forms import ModelForm
from .models import Person, Group


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob', 'sex']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
