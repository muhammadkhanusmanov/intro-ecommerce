from django.views import View
from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

# import models
from .models import (
    Product,
    Company,
    Category
)

def to_dict(product: Product) -> dict:
    '''convert product obj to dict'''
    return {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'color': product.color,
        'price': product.price,
        'company': product.company.id,
    }


class ProductView(View):
    def get(self, request: HttpRequest, id=None) -> JsonResponse:
        '''get products'''
        if id is None:
            # get all products
            products = Product.objects.all()

            # list of products
            products_list = [to_dict(product) for product in products]

            return JsonResponse(products_list, safe=False)
        else:
            try:
                product = Product.objects.get(id=id)
                return JsonResponse(to_dict(product))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def post(self, request:HttpRequest):
        """
            input data --> dictionary:
                {
                'name': name,
                'color': color,
                'price': price,
                'company': company_id
                }
            return result --> dictionary:
                {'result':'ok'}
        """
        ans=request.body.decode()
        data=json.loads(ans)
        name=data['name']
        color=data['color']
        price=data['price']
        company_id=data['company']
        try:
            company=Company.objects.get(id=company_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'does not exist'}, status=404)
        product=Product(name=name,color=color,price=price,company=company)
        product.save()
        return JsonResponse({'result':'ok'})

def update_product(request:HttpRequest,pk):
    if request.method == 'POST':
        """
        input data --> dictionary:
            {
            'name': name,
            'color': color,
            'price': price,
            'company': company_id
            }
        return --> dictionary
        """
        ans = request.body.decode()
        data = json.loads(ans)
        name = data['name']
        color = data['color']
        price = data['price']
        company_id = data['company']
        try:
            product = Product.objects.get(id=pk)
            product.name = name
            product.color = color
            product.price = price
            product.company = Company.objects.get(id=company_id)
            product.save()
            """
            return --> dictionary:
                {'result':'ok'}
            """
            return JsonResponse({'result':'ok'})
        except ObjectDoesNotExist:
            """
               return --> dictionary:
                   {'result':'Not existing product'}
            """
            return JsonResponse({'result':'Not existing product'}, status=404)
    else:
        return JsonResponse({'status': 'Method not allowed'})
        
