from django import forms
from django.forms import fields
from django.forms import widgets

class IDForm(forms.Form):
    def __init__(self,*args,**kw):
        forms.Form.__init__(self,*args,**kw)
        form_name = forms.CharField(max_length=32,
                                    required=True,
                                    widget=forms.HiddenInput,
                                    initial=self.__class__.__name__
                                   )
        self.fields["form_name"] = form_name



class CrimeSearchForm(IDForm):
    first_name = fields.CharField(required=False, max_length=42)
    last_name = fields.CharField(required=False, max_length=42)
    birthdate = fields.DateField(required=False, widget=widgets.DateInput)
    sid = forms.IntegerField(required=False)
    search_by_field = fields.MultipleChoiceField(
        required=False,
        widget=widgets.CheckboxSelectMultiple,
        choices=[("First Name", "first_name"),
                 ("Last Name", "last_name"),
                 ("Birth date", "birthdate"),
                 ("SID number", "sid")]
    )