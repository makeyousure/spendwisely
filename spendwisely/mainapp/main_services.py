from django.db.models import Sum

from incomes.models import IncomeOperation, SpendOperation, Account


def set_current_amount_of_account(account_id):
    incomes = IncomeOperation.objects.filter(income_acount=account_id).aggregate(Sum('income_amount'))
    spends = SpendOperation.objects.filter(spend_acount=account_id).aggregate(Sum('spend_amount'))
    start_money = Account.objects.filter(id=account_id)
    final_amount = start_money + spends + incomes
    return final_amount
