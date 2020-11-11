from django.contrib import admin
from .models import *


admin.site.register(SpendCategory)
admin.site.register(SpendArticle)
admin.site.register(Income)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')


class IncomeOperationAdmin(admin.ModelAdmin):
    list_display = ('income_date', 'income_article', 'income_acount', 'income_amount')


class SpendOperationAdmin(admin.ModelAdmin):
    list_display = ('spend_date', 'spend_article', 'spend_acount', 'spend_amount')


admin.site.register(IncomeOperation, IncomeOperationAdmin)
admin.site.register(SpendOperation, SpendOperationAdmin)
admin.site.register(Account, AccountAdmin)
