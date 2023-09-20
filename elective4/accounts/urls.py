from django.urls import path,include
from .views import AccounsListCreateView, AccounsUpdateDeleteView

urlpatterns = [
    path('fetch-create/', AccounsListCreateView.as_view(), name="accounts-list-create-view"),
    path('update-delete/<int:pk>/', AccounsUpdateDeleteView.as_view(), name="accounts-update-delete-view"),
]
