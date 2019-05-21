from django import forms


class NotificationForm(forms.Form):
    was_viewed = forms.BooleanField(initial=False)