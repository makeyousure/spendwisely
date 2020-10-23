from django.shortcuts import render, redirect

from incomes.models import SpendCategory, SpendArticle
from spends.forms import AddSpendCategory, AddSpendArticle


def show_all_spend_category(request):
    categories = SpendCategory.objects.all()
    context = {'categories': categories}
    return render(request, template_name='spends/spends_page.html', context=context)


def show_articles_filtered_by_category(request, spend_category_id):
    category = SpendCategory.objects.get(id=spend_category_id)
    articles_filtered_by_id = SpendArticle.objects.filter(category=spend_category_id)
    context = {'articles': articles_filtered_by_id,
               'category_name': category}
    return render(request, template_name='spends/spends_articles.html', context=context)


def delete_spend_category(request, spend_category_id):
    delete_spend_category_by_id = SpendCategory.objects.filter(id=spend_category_id).delete()
    context = {'delete_spend_category': delete_spend_category_by_id}
    return render(request, template_name='main/deleted.html', context=context)


def add_spend_category(request):
    if request.method == "POST":
        add_form_spend_category = AddSpendCategory(request.POST)
        if add_form_spend_category.is_valid():
            add_form_spend_category.save()
            return redirect('spend_page')
    else:
        add_form_spend_category = AddSpendCategory()
    context = {'add_form_spend_category': add_form_spend_category}
    return render(request, template_name='spends/add_spend_category.html', context=context)


def add_spend_article(request):
    if request.method == "POST":
        add_article = AddSpendArticle(request.POST)
        if add_article.is_valid():
            add_article.save()
            return redirect('add_spend_article')
    else:
        add_article = AddSpendArticle()
    context = {'add_article': add_article}
    return render(request, template_name='spends/add_spend_article.html', context=context)


def delete_spend_article(request, spend_article_id):
    delete_spend_article_by_id = SpendArticle.objects.filter(id=spend_article_id).delete()
    context = {'delete_article': delete_spend_article_by_id}
    return render(request, template_name="main/deleted.html", context=context)


