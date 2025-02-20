# Generated by Django 3.2.4 on 2021-06-27 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('airblue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Order position', 'verbose_name_plural': 'Order positions'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Product image', 'verbose_name_plural': 'Product images'},
        ),
        migrations.AlterModelOptions(
            name='productremains',
            options={'verbose_name': 'Product remains relation', 'verbose_name_plural': 'Product remains relations'},
        ),
        migrations.AlterModelOptions(
            name='productvariant',
            options={'verbose_name': 'Product variant', 'verbose_name_plural': 'Product variants'},
        ),
        migrations.AlterField(
            model_name='order',
            name='positions',
            field=models.ManyToManyField(through='airblue.OrderProduct', to='airblue.ProductRemains', verbose_name='related product remains'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='пользователи', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='amount',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Product amount'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='заказы', to='airblue.order', verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='productremains',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airblue.productremains', verbose_name='related product remains'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='variants',
            field=models.ManyToManyField(related_name='варианты', through='airblue.ProductRemains', to='airblue.ProductVariant', verbose_name='variant'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='картинки', to='airblue.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='url',
            field=models.URLField(verbose_name='Link to image'),
        ),
        migrations.AlterField(
            model_name='productremains',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='productremains',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='товары', to='airblue.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='productremains',
            name='productvariant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airblue.productvariant', verbose_name='variant'),
        ),
        migrations.AlterField(
            model_name='productremains',
            name='remains',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Remains amount'),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='категории', to='airblue.category', verbose_name='category'),
        ),
    ]
