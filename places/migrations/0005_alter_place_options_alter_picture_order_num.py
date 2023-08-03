# Generated by Django 4.2.3 on 2023-08-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_picture_options_alter_place_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['id'], 'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterField(
            model_name='picture',
            name='order_num',
            field=models.PositiveIntegerField(default=0),
        ),
    ]