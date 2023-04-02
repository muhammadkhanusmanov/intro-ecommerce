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



class ProductView(View):
    def get(self, request: HttpRequest, id=None) -> JsonResponse:
        '''get products'''
        if id is None:
            # get all products
            products = Product.objects.all()

            # list of products
            products_list = []
            for product in products:
                products_list.append(
                    {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'color': product.color,
                        'price': product.price,
                        'company': product.company.id,
                    }
                )
            return JsonResponse(products_list, safe=False)
        else:
            try:
                product = Product.objects.get(id=id)
                return JsonResponse(
                    {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'color': product.color,
                        'price': product.price,
                        'company': product.company.id,
                    })
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

def delete_product(request:HttpRequest,pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return JsonResponse({'result':'deleted'})
        except ObjectDoesNotExist:
            return JsonResponse({'result':'Not existing product'}, status=404)
    return JsonResponse({'status': 'Method not allowed'})

class CompanyView(View):
    def get(self, request:HttpRequest,id=None):
        if id==None:
            """
            input:
                nothing
            return:
                get all companies
            """
            companies = Company.objects.all()
            companies_list = []
            for company in companies:
                companies_list.append(
                    {
                        'id': company.id,
                        'name': company.name,
                        'website': company.website
                    }
                )
            return JsonResponse(companies_list, safe=False)
        else:
            try:
                company = Company.objects.get(id=id)
                return JsonResponse(
                    {
                    'id': company.id,
                    'name': company.name,
                    'website': company.website
                    }
                )
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'Not found company'}, status=404)
    def post(self, request:HttpRequest):
        """
        input data --> dictionary:
             {
             'name': name,
             'description': description,
             'website': website
             }
        return result --> dictionary:
            {'result':'ok'}
        """
        ans = request.body.decode()
        data=json.loads(ans)
        try:
            name=data['name']
            description=data['description']
            website=data['website']
        except:
            return JsonResponse({'result':'bad data'})
        company=Company(name=name, description=description, website=website)
        company.save()
        return JsonResponse({'result':'ok'})

def get_company_products(request:HttpRequest,id:int):
    if request.method == 'GET':
        try:
            company_id=Company.objects.get(id=id)
            products=Product.objects.filter(company=company_id)
            products_list=[]
            for product in products:
                products_list.append(
                    {
                        'id': product.id,
                        'name': product.name,
                        'description': product.description,
                        'color': product.color,
                        'price': product.price,
                        'company': product.company.id,
                    }
                )
            return JsonResponse(products_list, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'Not found company'}, status=404)
    return JsonResponse({'result':'Method not found'})



            
