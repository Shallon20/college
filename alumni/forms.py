from django import forms

from alumni.models import AlumniMessage



class AlumniMessageForm(forms.ModelForm):
    class Meta:
        model = AlumniMessage
        fields = '__all__'