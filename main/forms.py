from django.forms import ModelForm
from .models import *

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = '__all__'