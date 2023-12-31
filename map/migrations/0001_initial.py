# Generated by Django 4.2.7 on 2023-12-04 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('img', models.ImageField(height_field='height', upload_to='maps', verbose_name='Изображение карты', width_field='width')),
                ('width', models.PositiveIntegerField(blank=True, verbose_name='Ширина (пиксели)')),
                ('height', models.PositiveIntegerField(blank=True, verbose_name='Высота (пиксели)')),
            ],
            options={
                'verbose_name': 'План помещения',
                'verbose_name_plural': 'Планы помещений',
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.PositiveIntegerField(verbose_name='Координата по X')),
                ('y', models.PositiveIntegerField(verbose_name='Координата по Y')),
                ('employee', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workplace', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplaces', to='map.plan', verbose_name='Рабочее место')),
            ],
            options={
                'verbose_name': 'Рабочее место',
                'verbose_name_plural': 'Рабочие места',
            },
        ),
    ]
