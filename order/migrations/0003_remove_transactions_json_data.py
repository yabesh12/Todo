# Generated by Django 4.0.3 on 2022-03-15 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_transactions_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='json_data',
        ),
    ]
