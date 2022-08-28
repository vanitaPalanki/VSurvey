# Generated by Django 3.2.7 on 2021-10-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_addproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='pcategory',
            field=models.CharField(choices=[('Spices', 'Spices'), ('Chocklets', 'Chocklets'), ('Beverages', 'Beverages'), ('Tea & Coffee', 'Tea & Coffee'), ('Processed Fish', 'Processed Fish'), ('Processed oils', 'Processed oils'), ('Processed Meats', 'Processed Meats'), ('Bakery Products', 'Bakery Products'), ('Chips & Waffers', 'Chips & Waffers'), ('Processed Grains', 'Processed Grains'), ('Pastas & Noodles', 'Pastas & Noodles'), ('Milk & Milk Products', 'Milk & Milk Products'), ('Processed Sugar & Salt', 'Processed Sugar & Salt'), ('Packaged Fruits & Vegitables', 'Packaged Fruits & Vegitables'), ('Non of the above', 'Non of the above')], max_length=50),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='preferred_consumer',
            field=models.CharField(choices=[('All', 'All'), ('Infant/Newborn', 'Infant/Newborn'), ('Below 5 years', 'Below 5 years'), ('5 to 18 years', '5 to 18 years'), ('Above 18', 'Above 18'), ('Senior Citizen', 'Senior Citizen')], max_length=100),
        ),
    ]
