from dataclasses import fields
from .models import Task
from django.forms import ModelForm

class CreateForm(ModelForm):
    class Meta:
        model =Task
        fields ="__all__"
        exclude = ["user"]