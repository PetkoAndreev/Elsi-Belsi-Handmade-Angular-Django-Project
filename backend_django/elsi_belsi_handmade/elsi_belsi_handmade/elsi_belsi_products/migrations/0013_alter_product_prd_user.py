# Generated by Django 4.0.4 on 2022-04-21 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elsi_belsi_products', '0012_alter_product_prd_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prd_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
