# Generated by Django 4.0.4 on 2022-04-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elsi_belsi_auth', '0007_profile_facebook_url_profile_github_url_and_more'),
        ('elsi_belsi_products', '0010_alter_product_favorites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to='elsi_belsi_auth.profile'),
        ),
    ]
