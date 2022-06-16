from django.urls import path
from .views import CategoryListView, CategoryCreateView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('create/', CategoryCreateView.as_view())
]