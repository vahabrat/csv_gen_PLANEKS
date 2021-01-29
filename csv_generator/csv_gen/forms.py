from django import forms

from .models import Column


class ColumnForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ColumnForm, self).__init__(*args, **kwargs)

    class Meta:
         model = Column
         fields = ('column_type',)