# Generated by Django 3.2.7 on 2021-09-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]