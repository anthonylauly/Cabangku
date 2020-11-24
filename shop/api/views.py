from django.utils.text import slugify

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Shop
from .serializers import ShopSerializer
from .permissions import IsAdminOrIsSelf

class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated,]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsAdminOrIsSelf]
        
        return super(self.__class__, self).get_permissions()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['user'] = request.user.id
        serializer.initial_data['slug'] = slugify(request.data['name'])
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'], permission_classes=[IsAdminOrIsSelf])
    def myshop_list(self, request):
        user = request.user
        myshop = Shop.objects.filter(user=user)
        serializer = self.get_serializer(myshop, many=True)
        return Response(serializer.data)