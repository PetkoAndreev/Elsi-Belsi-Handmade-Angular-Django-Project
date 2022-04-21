import os
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken

from elsi_belsi_handmade import settings


# JWT tokens after login of the user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Custom permission IsAuthenticated for POST, PUT, PATCH and DELETE methods/requests
class HasRequiredPermissionForPostPutPatchDelete(permissions.BasePermission):
    post_permission_required = None
    put_permission_required = None
    patch_permission_required = None
    delete_permission_required = None

    def has_permission(self, request, view):
        if request.method.lower() in ('post', 'put', 'patch', 'delete'):
            permission_required_name = f'{request.method.lower()}_permission_required'
            permission_required = getattr(view, permission_required_name)
            if not request.user.is_authenticated:
                self.message = f'Access denied. You need to {permission_required} to access this service with {request.method} method!'
                return False
            return True
        return True


# Function to delete the old image or image when product deletion
def image_update_delete(product, request, method):
    default_image_name = f'default_product_image.png'
    # Get the image path
    image_path = os.path.abspath(os.path.join(settings.MEDIA_ROOT, str(product.prd_image)))
    # Check if the profile picture is not the default one and it's changed with a new one
    if method != 'delete' and default_image_name not in str(image_path) and 'prd_image' in request.data.keys():
        if request.data['prd_image']:
            os.remove(image_path)
    elif method == 'delete' and default_image_name not in str(image_path):
        os.remove(image_path)
