from rest_framework.permissions import BasePermission

#Permição dos usuarios

class IsProfessor(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user,'professor')
    
class IsAluno(BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user,'aluno')