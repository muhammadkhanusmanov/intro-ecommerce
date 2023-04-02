from django.urls import path
# import views
from .views import (
    ProductView,
    update_product
)

urlpatterns = [
   path('products', ProductView.as_view()), 
   path('products/<int:id>', ProductView.as_view()), 
   path('products/', ProductView.as_view()),
   path('products/<int:pk>/update/',update_product)
]