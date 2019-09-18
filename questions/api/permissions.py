from rest_framework import permissions

# Check is the user an author
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user