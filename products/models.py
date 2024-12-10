from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    PRODUCT_TYPES = [
        ("bouquet", "Букет"),
        ("sweet", "Сладость"),
        ("toy", "Игрушка"),
        ("greeting_card", "Открытка"),
        ("combo", "Комбо"),
    ]

    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products_images", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    product_type = models.CharField(max_length=32, choices=PRODUCT_TYPES)

    def __str__(self):
        return f"{self.name} ({self.get_product_type_display()})"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    




class Packaging(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Оформление"
        verbose_name_plural = "Оформление"

    def __str__(self):
        return self.name


# Дополнительные свойства для букетов
class Bouquet(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="bouquets"
    )
    description = models.TextField(blank=True, null=True)
    packaging = models.ForeignKey(
        Packaging, on_delete=models.CASCADE, related_name="bouquets"
    )

    class Meta:
        verbose_name = "Букет"
        verbose_name_plural = "Букеты"

    def __str__(self):
        return self.product.name


class BouquetOption(models.Model):
    bouquet = models.ForeignKey(
        Bouquet, related_name="options", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.bouquet.product.name} - {self.quantity} шт."


# Дополнительные свойства для сладостей
class Sweet(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="sweets"
    )
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Сладость"
        verbose_name_plural = "Сладости"

    def __str__(self):
        return f"{self.product.name} - {self.quantity} шт."

    # Метод который отображают все сладости
    @staticmethod
    def get_list_sweets():
        return Sweet.objects.select_related("product").all()


class Toy(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="toys"
    )

    class Meta:
        verbose_name = "Игрушка"
        verbose_name_plural = "Игрушки"

    def __str__(self):
        return self.product.name

    # Метод который отображают все игрушки
    @staticmethod
    def get_list_toys():
        return Toy.objects.select_related("product").all()


class GreetingCard(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="cards"
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Открытка"
        verbose_name_plural = "Открытки"

    def __str__(self):
        return self.product.name

    # Метод который отображают все открытки
    @staticmethod
    def get_list_cards():
        return GreetingCard.objects.select_related("product").all()
    


class Combo(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="combos"
    )
    bouquet = models.ForeignKey(
        Bouquet, on_delete=models.CASCADE, related_name="combos"
    )
    sweet = models.ForeignKey(Sweet, on_delete=models.CASCADE, related_name="combos")
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Комбо"
        verbose_name_plural = "Комбо"

    def __str__(self):
        return f"{self.product.name} - {self.bouquet.product.name} - {self.sweet.product.name} "
