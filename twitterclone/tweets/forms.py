from django import forms


class TwangForm(forms.Form):
    tweet = forms.CharField(max_length=140, widget=forms.Textarea)