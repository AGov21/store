from decimal import Decimal
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bouquet, BouquetOption
from products.models import Category, Product, Bouquet, Sweet, Toy, Combo, GreetingCard


class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"


class ProductDetaileView(DetailView):
    model = Product
    template_name = "products/product.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()

        if product.product_type == 'greeting_card':
            related_name = 'cards'
        else:
            related_name = f"{product.product_type}s"
        
        context[product.product_type] = getattr(product, related_name, None)
        context["list_sweets"] = Sweet.get_list_sweets()
        context["list_cards"] = GreetingCard.get_list_cards()
        context["list_toys"] = Toy.get_list_toys()

        return context


class CategoriesListTemplate(ListView):
    model = Category
    template_name = "products/categories.html"
    context_object_name = "categories"


class CategoryDetaileTemplate(DetailView):
    model = Category
    template_name = "products/category.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()  # Получаем текущую категорию
        context["products"] = Product.objects.filter(
            category=category
        )  # Фильтруем продукты по категории
        return context


class HomeTemplate(TemplateView):
    template_name = "products/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["bouquets"] = Bouquet.objects.all()

        return context