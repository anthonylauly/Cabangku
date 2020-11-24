from rest_framework import permissions

class IsAdminOrIsSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return  True
        elif request.user.is_superuser :
            return True
        
        return False