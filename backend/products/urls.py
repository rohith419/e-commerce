from django.urls import path
from .views import ProductListCreate, ProductRetrieve

urlpatterns = [
    path('', ProductListCreate.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductRetrieve.as_view(), name='product-detail'),
]
