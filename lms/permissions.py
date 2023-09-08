from rest_framework.permissions import BasePermission


class IsStaff(BasePermission):
    """Модератор может все кроме удаления и создания объектов"""

    def has_permission(self, request, view):
        if request.user.is_staff:
            if request.method in ['DELETE', 'POST']:
                return False

            return True


class IsOwner(BasePermission):
    """Права доступа пользователя"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
