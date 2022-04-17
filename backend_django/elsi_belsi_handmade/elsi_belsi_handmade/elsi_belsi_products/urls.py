from django.urls import path

from elsi_belsi_handmade.elsi_belsi_products.views import SimpleView

urlpatterns = (
    path('test/', SimpleView.as_view()),
)
