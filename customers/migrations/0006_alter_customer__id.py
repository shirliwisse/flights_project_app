# Generated by Django 4.0.5 on 2022-07-22 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer__id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
