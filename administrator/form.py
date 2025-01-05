from django import forms
from django.forms import ModelForm


from .models import *


class Edit_post(forms.ModelForm):
    class Meta:
        model = PostTable
        fields = ['type', 'workoutday', 'name','name','description']