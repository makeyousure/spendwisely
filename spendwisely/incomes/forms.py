from django import forms

from incomes.models import Income


class CreateIncomeCategory(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"