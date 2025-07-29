from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an Online store page, made in Django",
            "author": "Developed by: Felipe Agudelo Posada"
        })
        return context


class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 499.99},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999.99},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 49.99},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 89.99}
    ]


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {
            "title": "Products - Online Store",
            "subtitle": "List of products",
            "products": Product.products
        }
        return render(request, self.template_name, viewData)

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product = Product.products[int(id)-1]
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse("home"))

        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product
        }
        return render(request, self.template_name, viewData)

    
class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")

        errors = []

        try:
            price = float(price)
            if price <= 0:
                errors.append("Price must be positive.")
        except:
            errors.append("Price must be a valid number.")

        if errors:
            viewData = {
                "title": "Create product",
                "subtitle": "Product creation",
                "errors": errors
            }
        else:
            # ID automático = tamaño actual + 1
            new_id = str(len(Product.products) + 1)
            Product.products.append({
                "id": new_id,
                "name": name,
                "description": description,
                "price": price
            })

            viewData = {
                "title": "Create product",
                "subtitle": "Product successfully created",
                "product": {
                    "name": name,
                    "description": description,
                    "price": price
                }
            }

        return render(request, self.template_name, viewData)
