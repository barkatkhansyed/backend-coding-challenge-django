from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Add/Edit/Delete permissions are only allowed to the owner of the note.
        """
        return obj.owner == request.user
