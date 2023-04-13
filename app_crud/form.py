from django import forms


class CreateNew(forms.Form):
    title= forms.CharField(label="title", max_length=50)
    description = forms.CharField(label="description", widget=forms.Textarea)