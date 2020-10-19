from django import forms

from spends.models import Account


class CreateAccForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
