from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

UserModel = get_user_model()


class Product(models.Model):
    TYPE_CHOICE_CARDS = 'Cards'
    TYPE_CHOICE_JEWELRY = 'Jewelry'
    TYPE_CHOICE_PAINTINGS = 'Paintings'
    TYPE_CHOICE_WOODEN_TOYS = 'Wooden Toys'

    CATEGORY_CHOICES = (
        (TYPE_CHOICE_CARDS, 'Cards'),
        (TYPE_CHOICE_JEWELRY, 'Jewelry'),
        (TYPE_CHOICE_PAINTINGS, 'Paintings'),
        (TYPE_CHOICE_WOODEN_TOYS, 'Wooden Toys'),
    )

    product_name = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )

    prd_category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=TYPE_CHOICE_CARDS,
    )
    prd_description = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
    )
    prd_image = models.ImageField(
        upload_to='products',
    )
    prd_date_added = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Added"
    )
    prd_date_updated = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date Updated"
    )
    prd_price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        validators=[
            MinValueValidator(Decimal('0.01')),
        ]
    )
    # prd_likes = models.ManyToManyField(
    #     UserModel,
    #     related_name='product_likes',
    #     blank=True)
    prd_user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    ),
    favourites = models.ManyToManyField(
        UserModel,
        related_name='product_favourite',
        blank=True
    )

    # str method visualize data in admin panel as row, not as columns
    def __str__(self):
        return f'{self.product_name}, {self.prd_description}, {self.prd_price}'


class Like(models.Model):
    # When we have FK an object is created in main class - Model_Name_set
    # in our case - like_set is the name of the object and in that way we get the likes
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
