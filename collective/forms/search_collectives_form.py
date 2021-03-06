from __future__ import unicode_literals

from django import forms

from ..services import get_active_tags

def get_choices():
    return [(tag.pk, tag.name) for tag in get_active_tags()]

class SearchCollectivesForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"id": "name", "class": "form-control"})
    )
    tags = forms.MultipleChoiceField(
        choices=get_choices,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
