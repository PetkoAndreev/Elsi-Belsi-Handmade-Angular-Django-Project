# Generated by Django 4.0.4 on 2022-04-21 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elsi_belsi_auth', '0007_profile_facebook_url_profile_github_url_and_more'),
        ('elsi_belsi_products', '0011_alter_product_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prd_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elsi_belsi_auth.profile'),
        ),
    ]
