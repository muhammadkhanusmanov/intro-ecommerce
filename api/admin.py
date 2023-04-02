from django.contrib import admin
from .models import Product, Category, Company

admin.site.register([Product, Company, Category])

