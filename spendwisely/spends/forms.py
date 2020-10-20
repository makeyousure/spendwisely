from django import forms

from incomes.models import SpendCategory, SpendArticle


class AddSpendCategory(forms.ModelForm):
    class Meta:
        model = SpendCategory
        fields = "__all__"


class AddSpendArticle(forms.ModelForm):
    class Meta:
        model = SpendArticle
        fields = "__all__"
