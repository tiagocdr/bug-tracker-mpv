from django import forms

class TicketForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(
        max_length=250,
        widget=forms.Textarea
        )
    