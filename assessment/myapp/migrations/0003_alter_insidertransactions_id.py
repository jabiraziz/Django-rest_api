# Generated by Django 4.1.2 on 2022-12-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_stock_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insidertransactions',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
