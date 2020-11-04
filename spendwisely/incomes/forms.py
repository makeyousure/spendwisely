from django import forms

from incomes.models import Income, IncomeOperation, Account


class CreateIncomeCategory(forms.ModelForm):
    class Meta:
        model = Income
        fields = "__all__"


class CreateIncomeOperation(forms.ModelForm):

    class Meta:
        model = IncomeOperation
        fields = "__all__"
        widgets = {
            'income_date': forms.DateInput(attrs={'class': 'operation_date_form'}),
            'income_article': forms.Select(attrs={'class': 'operation_article_form'}),
            'income_acount': forms.Select(attrs={'class': 'operation_acount_form'}),
            'income_amount': forms.NumberInput(attrs={'class': 'operation_amount_form'}),
            'comment_for_income_operation': forms.TextInput(attrs={'class': 'operation_comment_form'})
        }

