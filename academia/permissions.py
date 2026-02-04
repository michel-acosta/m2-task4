from rest_framework.permissions import BasePermission, SAFE_METHODS


class EsProfesor(BasePermission):
    """
    Permite acceso solo a usuarios del grupo 'Profesores'.
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Profesores').exists()


class SoloProfesoresEscritura(BasePermission):
    """
    Permite lectura a cualquier usuario autenticado,
    pero escritura solo a profesores.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Profesores').exists()
