from django import forms

from incomes.models import SpendCategory, SpendArticle, SpendOperation


class AddSpendCategory(forms.ModelForm):
    class Meta:
        model = SpendCategory
        fields = "__all__"


class AddSpendArticle(forms.ModelForm):
    class Meta:
        model = SpendArticle
        fields = "__all__"


class CreateSpendOperation(forms.ModelForm):

    class Meta:
        model = SpendOperation
        fields = "__all__"
        widgets = {
            'spend_date': forms.DateInput(attrs={'class': 'operation_date_form'}),
            'spend_article': forms.Select(attrs={'class': 'operation_article_form'}),
            'spend_acount': forms.Select(attrs={'class': 'operation_acount_form'}),
            'spend_amount': forms.NumberInput(attrs={'class': 'operation_amount_form'}),
            'comment_for_spend_operation': forms.TextInput(attrs={'class': 'operation_comment_form'})
        }