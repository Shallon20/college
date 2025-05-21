from django import forms
from .models import HostelApplication

class HostelApplicationForm(forms.ModelForm):
    class Meta:
        model = HostelApplication
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Any medical conditions, preferences...'}),
            'preferred_type': forms.Select(choices=[
                ('2-Bed Room', '2-Bed Room'),
                ('4-Bed Room', '4-Bed Room'),
                ('6-Bed Room', '6-Bed Room')
            ])
        }
