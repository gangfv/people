from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())


class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())