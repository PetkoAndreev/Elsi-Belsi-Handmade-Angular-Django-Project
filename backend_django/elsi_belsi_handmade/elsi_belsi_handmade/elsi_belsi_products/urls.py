from django.urls import path

from elsi_belsi_handmade.elsi_belsi_products.views import ProductsListCreateView, \
    ProductListUpdateDeleteView, FavoriteView, LikeView

urlpatterns = [
    # path('test/', SimpleView.as_view()),
    path('', ProductsListCreateView.as_view(), name='api list or create products'),
    path('<int:pk>/', ProductListUpdateDeleteView.as_view(), name='api product details'),
    path('<int:pk>/add-to-favorites/', FavoriteView.as_view(), name='favorite add remove'),
    path('<int:pk>/likes/', LikeView.as_view(), name='like unlike product'),
]
