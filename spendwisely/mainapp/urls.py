from django.urls import path

from . import views


urlpatterns = [
    path('create-account/', views.add_account, name='add_account'),
    path('delete-account/<int:account_id>/', views.delete_some_account, name='delete_acc'),
    path('', views.show_main_page, name='main_page'),
]