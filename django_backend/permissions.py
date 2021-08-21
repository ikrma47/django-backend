from rest_framework import permissions
from rest_framework import status


class IsAdmin(permissions.BasePermission):

    message = "Only Admin is Allowed to do this"
    code = status.HTTP_405_METHOD_NOT_ALLOWED

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.isAdmin
        )
