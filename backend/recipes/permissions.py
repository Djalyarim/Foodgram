from rest_framework import permissions


class IsAuthorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if (request.method == 'POST' or request.user.is_superuser
               or obj.author == request.user):
                return True
        return request.method in permissions.SAFE_METHODS
