from django.urls import path

from incomes import views

urlpatterns = [
    path('income-operations/', views.show_income_operations_list, name='list_of_income_operations'),

    path('create-income-category/', views.add_income_category, name='create_income_category'),

    path('delete-income-category/<int:category_id>/', views.delete_someone_category_of_income,
         name='delete_income_category'),

    path('', views.show_all_inclome_category, name='incomes_page'),
]