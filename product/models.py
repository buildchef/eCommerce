from django.conf import settings
from django.db import models
from django.utils.text import slugify
from PIL import Image

from utils import utils

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    marketing_price = models.FloatField(default=0, verbose_name='Price')
    marketing_price_promotional = models.FloatField(default=0, verbose_name='Promotional price')
    type = models.CharField(
        default='V',
        max_length=1,
        choices=(
        ('V', 'Variation'),
        ('S', 'Simple')
        )
    )   

    def get_formatted_price(self):
        return utils.format_price(self.marketing_price)
    get_formatted_price.short_description = 'Price'

    def get_formatted_price_promotional(self):
        return utils.format_price(self.marketing_price_promotional)
    get_formatted_price_promotional.short_description = 'Promotional price'

    @staticmethod
    def resize_image(img, new_widht=800):
        img_full_path = settings.MEDIA_ROOT / img.name
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size
        
        if original_width >= new_widht:
            img_pill.close()
            return 
        
        new_height = round((new_widht * original_height) / original_width)

        new_img  = img_pill.resize((new_widht, new_height), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.name)}'
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name