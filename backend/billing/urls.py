# billing/urls.py

from django.urls import path
from .views import (
    SavingsSummaryView,
    SavingsResourceBreakdownView,
    SavingsInvoiceView,
)

urlpatterns = [
    path("summary", SavingsSummaryView.as_view()),
    path("resources", SavingsResourceBreakdownView.as_view()),
    path("invoice", SavingsInvoiceView.as_view()),
]
