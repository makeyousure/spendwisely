from datetime import datetime

from incomes.models import SpendOperation, SpendArticle


def show_info_about_today():
    filter_spends_by_today = SpendOperation.objects.filter(spend_date=datetime.date(datetime.today()))
    count_of_spends = len(filter_spends_by_today)
    if count_of_spends == 0:
        return 'ВЫ ЕЩЕ НЕ ВНОСИЛИ РАСХОДЫ'
    total_amount_for_today = 0
    for operation in filter_spends_by_today:
        total_amount_for_today += operation.spend_amount

    return 'СЕГОДНЯ ТЫ ВНЕС {} РАСХОДОВ НА СУММУ {} РУБЛЕЙ'.format(count_of_spends, total_amount_for_today)
