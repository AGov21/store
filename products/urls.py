from django.urls import path
from products.views import (
    CategoriesListTemplate,
    ProductListView,
    ProductDetaileView,
    CategoryDetaileTemplate,
    ContactTemplate
)

app_name = "products"
urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("product/<int:pk>/", ProductDetaileView.as_view(), name="product"),
    path("category/<int:pk>/", CategoryDetaileTemplate.as_view(), name="category"),
    path("categories/", CategoriesListTemplate.as_view(), name="categories"),
    path('contact/', ContactTemplate.as_view(), name='contact')

]
