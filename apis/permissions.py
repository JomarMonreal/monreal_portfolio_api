from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyOrIsAuthenticated(BasePermission):
    """
    Custom permission to only allow authenticated users to edit objects,
    but allow read-only access to unauthenticated users.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
