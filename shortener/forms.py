from django import forms
from .models import ShortenedURL
from django.core.exceptions import ValidationError
class ShortenerForm(forms.ModelForm):
    # Overriding fields to add Bootstrap styling (CSS Classes)
    original_url = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Paste your long URL here...'
    }))
    
    short_code = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Custom code (optional)'
    }))
    def clean_short_code(self):
        short_code = self.cleaned_data.get('short_code')
        if short_code and ShortenedURL.objects.filter(short_code=short_code).exists():
            raise ValidationError("This custom code is already taken. Please try another.")
        return short_code

    class Meta:
        model = ShortenedURL
        fields = ['original_url', 'short_code']