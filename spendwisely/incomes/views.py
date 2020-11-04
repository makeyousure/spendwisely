from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import CreateIncomeCategory, CreateIncomeOperation
from .models import Income, IncomeOperation


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
    return render(request, template_name='incomes/add_income_category.html',
                  context={'add_form_income': add_form_income})


def show_income_operations_list(request):
    if request.method == "POST":
        add_income_operation_form = CreateIncomeOperation(request.POST)
        if add_income_operation_form.is_valid():
            add_income_operation_form.save()
            return redirect('list_of_income_operations')
    else:
        add_income_operation_form = CreateIncomeOperation()
    all_income_operations = IncomeOperation.objects.all().order_by('-income_date')
    paginator = Paginator(all_income_operations, 10)
    page_number = request.GET.get('page')
    incomes_pages = paginator.get_page(page_number)
    context = {"income_operarions": incomes_pages, 'add_income_form': add_income_operation_form}
    return render(request, template_name='incomes/income_operations.html', context=context)
