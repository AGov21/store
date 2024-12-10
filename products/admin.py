from django.contrib import admin
from products.models import Category, Product, Bouquet, Sweet, Toy, GreetingCard, Packaging, Combo, BouquetOption


admin.site.register(Category)
admin.site.register(Toy)
admin.site.register(Product)
admin.site.register(Bouquet)
admin.site.register(BouquetOption)
admin.site.register(Sweet)
admin.site.register(GreetingCard)
admin.site.register(Combo)
admin.site.register(Packaging)
