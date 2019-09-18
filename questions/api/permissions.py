from rest_framework import permissions

# Check is the user an author
class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):

        # Check permissions for read-only request
        if request.method in permissions.SAFE_METHODS:
            print(request.method)
            print(request.user)
            return True

        # Check permissions for write request
        return obj.author == request.user