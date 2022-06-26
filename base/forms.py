
from django.forms import ModelForm

from base.models import Lead


class LeadForm(ModelForm):
    class Meta: 
        model = Lead
        fields = '__all__'

