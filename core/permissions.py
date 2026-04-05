from rest_framework.permissions import BasePermission


class IsAuthenticatedAndRole(BasePermission):
    """
    Base class to check authentication + role
    """
    allowed_roles = []

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return getattr(user, "role", None) in self.allowed_roles


class IsAdmin(IsAuthenticatedAndRole):
    allowed_roles = ['admin']


class IsAnalystOrAdmin(IsAuthenticatedAndRole):
    allowed_roles = ['analyst', 'admin']


class IsViewer(IsAuthenticatedAndRole):
    allowed_roles = ['viewer']


class IsViewerOrAbove(IsAuthenticatedAndRole):
    allowed_roles = ['viewer', 'analyst', 'admin']