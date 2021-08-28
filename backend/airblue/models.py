from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name=_('Name'),
    )
    parent_prefix = models.CharField(
        max_length=128,
        verbose_name=_('Parent prefix'),
        default=gettext('Uncategorized')
    )

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = _('Product category')
        verbose_name_plural = _('Product categories')


class ProductVariant(models.Model):

    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name=_('Name'),
    )
    style = models.JSONField(
        default=dict,
        verbose_name=_('Style'),
    )

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = _('Product variant')
        verbose_name_plural = _('Product variants')


class Product(models.Model):

    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name=_('Name'),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_('Description'),
    )
    variants = models.ManyToManyField(
        ProductVariant,
        through='ProductRemains',
        related_name='products',
        verbose_name=_('variant'),
    )
    categories = models.ManyToManyField(
        Category,
        related_name='products',
        verbose_name=_('categories'),
    )

    def __str__(self):

        return self.name

    class Meta:

        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductRemains(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='remains',
        verbose_name=_('product'),
    )
    productvariant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        verbose_name=_('variant'),
    )
    remains = models.PositiveSmallIntegerField(
        default=1,
        verbose_name=_('Remains amount'),
    )
    price = models.PositiveIntegerField(
        verbose_name=_('Price'),
    )

    def __str__(self):

        return _('Remains: %(product)s (%(variant)s)') % {
            'product': self.product.name, 'variant': self.productvariant.name
        }

    class Meta:

        verbose_name = _('Product remains relation')
        verbose_name_plural = _('Product remains relations')
        unique_together = ['product', 'productvariant']


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('product'),
        related_name='images',
    )
    url = models.URLField(
        verbose_name=_('Link to image'),
        max_length=300,
    )

    def __str__(self):

        return _('Image:  %(product)s') % {
            'product': self.product.name,
        }

    class Meta:

        verbose_name = _('Product image')
        verbose_name_plural = _('Product images')


class Order(models.Model):

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        related_name='orders',
        verbose_name=_('user'),
    )
    positions = models.ManyToManyField(
        ProductRemains,
        through='OrderProduct',
        verbose_name=_('related product remains'),
    )

    class Meta:

        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class OrderProduct(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='orderproducts',
        verbose_name=_('order'),
    )
    productremains = models.ForeignKey(
        ProductRemains,
        on_delete=models.CASCADE,
        verbose_name=_('related product remains'),
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        verbose_name=_('Product amount'),
    )

    class Meta:

        verbose_name = _('Order position')
        verbose_name_plural = _('Order positions')
