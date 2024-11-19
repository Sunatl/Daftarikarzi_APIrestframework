# views.py
from rest_framework import generics
from .models import *
from .serialaizer import *

# Customer 
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Wallet 
class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class WalletDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


# Loan
class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  # Параметри ҷустуҷӯ
        if query:
            queryset = queryset.filter(
                Q(customer__name__icontains=query) |  # Ҷустуҷӯ бо номи мизоҷ
                Q(description__icontains=query) |    # Ҷустуҷӯ бо тавсиф
                Q(total_amount__icontains=query)     # Ҷустуҷӯ бо маблағи умумӣ
            )
        return queryset

class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

# Payment 
class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
