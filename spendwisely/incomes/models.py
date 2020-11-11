from django.db import models
from django.utils import timezone


class SpendCategory(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории расходов"


class SpendArticle(models.Model):
    name = models.CharField(verbose_name="Название статьи расходов", max_length=50)
    category = models.ForeignKey(SpendCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Статьи расходов"


class Income(models.Model):
    name = models.CharField(verbose_name="Статья доходов", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Доходы"


class Account(models.Model):
    name = models.CharField(verbose_name="Счет", max_length=50)
    amount = models.DecimalField(verbose_name="Остаток", max_digits=10, decimal_places=2, default=0)

    def change_amount(self):
        start_amount = self.amount

        get_income_operation_by_id = IncomeOperation.objects.filter(income_acount=self.id)
        get_spend_operation_by_id = SpendOperation.objects.filter(spend_acount=self.id)

        for operation in get_income_operation_by_id:
            start_amount += operation.income_amount

        for operation in get_spend_operation_by_id:
            start_amount -= operation.spend_amount

        return start_amount

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Счета"


class IncomeOperation(models.Model):
    income_date = models.DateTimeField(verbose_name="Дата", default=timezone.now())
    income_article = models.ForeignKey(Income, verbose_name="Статья дохода", on_delete=models.SET_NULL,
                                       null=True, blank=True)
    income_acount = models.ForeignKey(Account, verbose_name="Счет зачисления", on_delete=models.SET_NULL,
                                      null=True, blank=True)
    income_amount = models.DecimalField(verbose_name="Сумма дохода", max_digits=10, decimal_places=2, default=0)
    comment_for_income_operation = models.CharField(max_length=500, verbose_name="Комментарий", default='', blank=True)

    class Meta:
        verbose_name_plural = "Доходные операции"


class SpendOperation(models.Model):
    spend_date = models.DateTimeField(verbose_name="Дата", default=timezone.now())
    spend_article = models.ForeignKey(SpendArticle, verbose_name="Статья расхода", on_delete=models.SET_NULL,
                                      null=True, blank=True)
    spend_acount = models.ForeignKey(Account, verbose_name="Счет списания", on_delete=models.SET_NULL,
                                     null=True, blank=True)
    spend_amount = models.DecimalField(verbose_name="Сумма списания", max_digits=10, decimal_places=2, default=0)
    comment_for_spend_operation = models.CharField(max_length=500, verbose_name="Комментарий", default='', blank=True)

    class Meta:
        verbose_name_plural = "Расходные операции"
