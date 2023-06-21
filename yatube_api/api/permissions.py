from rest_framework import permissions


class AuthorOrAuthorization(permissions.BasePermission):
    """
    Список объектов доступен всем пользователям.
    Создание объекта достуно авторизированным пользователям.
    Редактирование/удаление объекта доступно только автору объекта.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
