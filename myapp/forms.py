from django import forms
from .models import Feedback  # import your Feedback model

class feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'age', 'movie', 'email', 'feed']
