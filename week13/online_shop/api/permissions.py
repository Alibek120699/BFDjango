from rest_framework.permissions import BasePermission

from .constants import SALESMAN, CUSTOMER


class IsAllowedToCreateProduct(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == SALESMAN


class IsAllowedToCreateOrder(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == CUSTOMER
