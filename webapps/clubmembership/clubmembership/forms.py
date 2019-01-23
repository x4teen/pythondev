from django.forms import ModelForm
from .models import Person, Group, Fee


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'dob', 'sex']


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'started']


class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = ['group', 'description', 'amount', 'period', 'effective']
