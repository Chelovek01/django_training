from django.forms import ModelForm

from .models import Bb


class BbForms(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
