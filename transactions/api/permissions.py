from rest_framework import permissions

class IsAdminOrShopOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.shop.user:
            return True
        elif request.user.is_staff:
            return True

        return False

class IsAdminOrBuyer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.buyer:
            return True
        elif request.user.is_staff:
            return True
        
        return False
