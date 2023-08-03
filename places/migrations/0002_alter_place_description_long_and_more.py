# Generated by Django 4.2.3 on 2023-08-01 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=models.TextField(null=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=16, max_digits=20, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='long',
            field=models.DecimalField(decimal_places=16, max_digits=20, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='Картинка')),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pictures', to='places.place', verbose_name='Место')),
            ],
        ),
    ]