# Generated by Django 3.2 on 2021-04-30 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_productinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Product_images '),
        ),
    ]