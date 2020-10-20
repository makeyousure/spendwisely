from django.urls import path, include

from spends import views

urlpatterns = [
    path('article/<str:spend_category_id>/', views.show_articles_filtered_by_category, name='show_article'),
    path('delete-spend-article/<int:spend_article_id>/', views.delete_spend_article, name='delete_spend_article'),
    path('create-spend-article/', views.add_spend_article, name='add_spend_article'),
    path('create-spend-category/', views.add_spend_category, name='add_spend_category'),
    path('delete-spend-category/<int:spend_category_id>/', views.delete_spend_category, name='delete_spend_category'),
    path('', views.show_all_spend_category, name='spend_page')
]
