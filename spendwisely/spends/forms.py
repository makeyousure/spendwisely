from django import forms

from spends.models import Income


class CreateIncomeCategory(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"