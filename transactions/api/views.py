from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from ..models import TransactionModels
from .serializers import TransactionSerializer
from .permissions import IsAdminOrShopOwner, IsAdminOrBuyer

class TransactionViewSet(ModelViewSet):
    queryset = TransactionModels.objects.all()
    serializer_class = TransactionSerializer
    
    def get_permissions(self):
        if self.action in ['create']:
            self.permissions_classes = [IsAdminOrShopOwner]
        elif self.action in ['list', 'update', 'partial_update']:
            self.permissions_classes = [IsAdminUser()]
        elif self.action in ['retrieve']:
            self.permissions_classes = [IsAdminOrShopOwner, IsAdminOrBuyer]

        return super(self.__class__, self).get_permissions()