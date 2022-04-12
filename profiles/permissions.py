from rest_framework.permissions import BasePermission, SAFE_METHODS

class ProfileUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the own user only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            # Check permissions for read-only request
            return True

        # Only owner of post can have write/update access
        return obj.user == request.user