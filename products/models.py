from django.db import models


# Создаём таблицу для категории
class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Создаём таблицу для Продуктов
class ProductModel(models.Model):
    title = models.CharField(max_length=100, help_text='Тут вы должны написать название вашего продукта')
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='product_images')
    descriptions = models.TextField()
    count = models.IntegerField(default=0)
    link = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


# Создать таблицу(модель) для карзины -> product(ForeignKey), total_price, total_count, created_at
# class CartModel()


class CartModel(models.Model):
    product = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Cart Models"


class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "News Categories"


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"
