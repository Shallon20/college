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
class EnrollmentForm(forms.Form):
    full_name = forms.CharField(max_length=100, label="Full Name")
    email = forms.EmailField(label="Email Address")
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    course = forms.ChoiceField(
        choices=[
            ('', 'Select a course'),
            ('Business Management', 'Business Management'),
            ('Computer Science', 'Computer Science'),
            ('Nursing', 'Nursing'),
            ('Education', 'Education'),
        ],
        label="Course Interested In"
    )
    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 5,
            'placeholder': 'Tell us briefly...'
        }),
        label="Why do you want to join Ushindi College?"
    )