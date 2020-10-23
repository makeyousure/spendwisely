from django.shortcuts import render, redirect

from .forms import CreateIncomeCategory
from .spends_services import *


def show_all_inclome_category(request):
    all_category = Income.objects.all()
    context = {'categories': all_category}
    return render(request, 'incomes/incomes_page.html', context=context)


def delete_someone_category_of_income(request, category_id):
    delete_category_by_id = Income.objects.filter(id=category_id).delete()
    context = {'delete_category': delete_category_by_id}
    return render(request, 'main/deleted.html', context=context)


def add_income_category(request):
    if request.method == "POST":
        add_form_income = CreateIncomeCategory(request.POST)
        if add_form_income.is_valid():
            add_form_income.save()
            return redirect('incomes_page')
    else:
        add_form_income = CreateIncomeCategory()
    return render(request, template_name='incomes/add_income_category.html', context={'add_form_income': add_form_income})

