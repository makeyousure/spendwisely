from django import forms

from incomes.models import Account


class CreateAccForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
