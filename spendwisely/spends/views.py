from django.shortcuts import render, redirect

from .forms import CreateIncomeCategory
from .spends_services import *


def show_all_inclome_category(request):
    all_category = Income.objects.all()
    context = {'categories': all_category}
    return render(request, 'spends/incomes_page.html', context=context)


def delete_someone_category_of_income(request, category_id):
    delete_category_by_id = Income.objects.filter(id=category_id).delete()
    context = {'delete_category': delete_category_by_id}
    return render(request, 'spends/income_deleted_category.html', context=context)


def add_income_category(request):
    if request.method == "POST":
        form = CreateIncomeCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incomes_page')
    else:
        form = CreateIncomeCategory()
    return render(request, template_name='spends/add_income_category.html', context={'form': form})

