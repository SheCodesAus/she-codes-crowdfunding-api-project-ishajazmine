from rest_framework import permissions

# the function makes sure person trying to change the object is also the person who owns the object
# can we let ADMIN edit? 
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user