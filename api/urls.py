from django.urls import path
# import views
from .views import (
    ProductView,
    update_product,
    delete_product,
    CompanyView,
    get_company_products
)

urlpatterns = [
   path('products', ProductView.as_view()), 
   path('products/<int:id>', ProductView.as_view()), 
   path('products/', ProductView.as_view()),
   path('products/<int:pk>/update/',update_product),
   path('products/<int:pk>/delete/',delete_product),
   path('companies/', CompanyView.as_view()),
   path('companies/<int:id>',CompanyView.as_view()),
   path('companies/<int:id>/products/',get_company_products)
]