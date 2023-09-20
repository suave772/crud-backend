from rest_framework import generics
from .serializers import AccountsSerializer
from .models import Account

class AccounsListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

class AccounsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

