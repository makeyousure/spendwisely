from django.shortcuts import render, redirect

from mainapp.forms import CreateAccForm
from incomes.models import Account, IncomeOperation, SpendOperation
from mainapp.main_services import show_info_about_today


def show_main_page(request):
    accounts = Account.objects.all()
    header = show_info_about_today()
    context = {"accounts": accounts, 'header': header}
    return render(request, template_name="main/mainpage.html", context=context)


def delete_some_account(request, account_id):
    delete_account_by_id = Account.objects.filter(id=account_id).delete()
    context = {"delete": delete_account_by_id}
    return render(request, template_name='main/deleted.html', context=context)


def add_account(request):
    if request.method == "POST":
        form = CreateAccForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = CreateAccForm()
    return render(request, template_name='main/add_account.html', context={'form': form})
