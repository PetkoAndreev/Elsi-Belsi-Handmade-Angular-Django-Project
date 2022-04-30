from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics as api_views, filters
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from elsi_belsi_handmade.elsi_belsi_products.models import Product
from elsi_belsi_handmade.elsi_belsi_products.serializers import ProductsListSerializer, ProductCreateSerializer, \
    ProductGetUpdateDeleteSerializer
from elsi_belsi_handmade.utils.utils import HasRequiredPermissionForPostPutPatchDelete, image_update_delete, get_payload

UserModel = get_user_model()


class ProductsListCreateView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [HasRequiredPermissionForPostPutPatchDelete]
    post_permission_required = 'logged in or to register an account to be able to create products and'
    query_filter_names = ('prd_category',)
    # Filter by field logic, search, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'product_name', 'prd_price']
    search_fields = ['product_name']
    ordering_fields = ['id', 'product_name', 'prd_category']

    list_serializer_class = ProductsListSerializer
    create_serializer_class = ProductCreateSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return self.create_serializer_class
        return self.list_serializer_class

    def perform_create(self, serializer):
        payload = get_payload(self.request)
        user = UserModel.objects.filter(pk=payload['user_id']).first()
        serializer.save(prd_user=user)


class ProductListUpdateDeleteView(api_views.RetrieveUpdateDestroyAPIView):
    permission_classes = [HasRequiredPermissionForPostPutPatchDelete]
    post_permission_required = 'be logged in or to register an account to be able to create products and'
    put_permission_required = 'be the owner of the product'
    patch_permission_required = 'be the owner of the product'
    delete_permission_required = 'be the owner of the product'

    queryset = Product.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = ProductGetUpdateDeleteSerializer

    def perform_update(self, serializer):
        # payload = get_payload(self.request)
        product = self.get_object()
        if self.request.user.id != product.prd_user_id:
            raise PermissionDenied(
                {'message': 'You are not the owner of the product and you can\'t perform UPDATE operation!'})
        else:
            image_update_delete(product, self.request, 'put/patch')
        serializer.save()

    def perform_destroy(self, instance):
        product = self.get_object()
        if self.request.user.id != product.prd_user_id:
            raise PermissionDenied(
                {'message': 'You are not the owner of the product and you can\'t perform DELETE operation!'})
        else:
            image_update_delete(product, self.request, 'delete')
        instance.delete()


class FavoriteView(APIView):
    http_method_names = ['post', ]
    model = Product
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs['pk'])
        # Check if the user is owner of the product
        if self.request.user.id != product.prd_user_id:
            if request.user.profile in product.favorites.all():
                product.favorites.remove(request.user.profile)
            else:
                product.favorites.add(request.user.profile)
            product.save()
        else:
            raise PermissionDenied(
                {'message': 'You are not the owner of the product and you can\'t perform ADD TO FAVORITES operation!'})
        return redirect('api product details', pk=self.kwargs['pk'])


class LikeView(APIView):
    http_method_names = ['post', ]
    model = Product
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs['pk'])
        # Check if the user is owner of the product
        if self.request.user.id != product.prd_user_id:
            if request.user.profile in product.likes.all():
                product.likes.remove(request.user.profile)
            else:
                product.likes.add(request.user.profile)
            product.save()
        else:
            raise PermissionDenied(
                {'message': 'You are not the owner of the product and you can\'t perform LIKE/DISLIKE operation!'})
        return redirect('api product details', pk=self.kwargs['pk'])
