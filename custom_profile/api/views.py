from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny

from .serializers import ProfileSerializer
from .permissions import IsAdminOrIsSelf
from ..models import Profile

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [IsAdminUser]
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
        if self.action in ['retrieve', 'partial_update']:
            self.permission_classes = [IsAdminOrIsSelf]

        return super(self.__class__, self).get_permissions()
    