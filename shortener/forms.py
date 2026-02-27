from django import forms
from .models import ShortenedURL

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

    class Meta:
        model = ShortenedURL
        fields = ['original_url', 'short_code']