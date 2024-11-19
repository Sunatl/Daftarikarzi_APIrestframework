# urls.py
from django.urls import path
from .views import *
urlpatterns = [
    # Customer URLs
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    # Wallet URLs
    path('wallets/', WalletListCreateView.as_view(), name='wallet-list-create'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),

    # Loan URLs
    path('loans/', LoanListCreateView.as_view(), name='loan-list-create'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),

    # Payment URLs
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
