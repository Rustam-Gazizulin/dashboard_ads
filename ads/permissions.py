from rest_framework import permissions


class IsOwnerOrModerator(permissions.BasePermission):
    message = 'Редактировать имеет право владелец или модератор'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in ['moderator']:
            return True
        return False
