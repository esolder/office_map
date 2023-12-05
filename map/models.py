import os

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


class Plan(models.Model):
    name = models.CharField('Наименование', max_length=200, unique=True)
    img = models.ImageField(
        'Изображение карты',
        upload_to='maps',
        width_field='width',
        height_field='height',
    )
    width = models.PositiveIntegerField('Ширина (пиксели)', blank=True)
    height = models.PositiveIntegerField('Высота (пиксели)', blank=True)

    class Meta:
        verbose_name = 'План помещения'
        verbose_name_plural = 'Планы помещений'

    def __str__(self):
        return self.name


class Workplace(models.Model):
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        related_name='workplaces',
        verbose_name='Рабочее место',
    )
    employee = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='workplace',
        verbose_name='Сотрудник',
        blank=True,
        null=True,
    )
    x = models.PositiveIntegerField('Координата по X')
    y = models.PositiveIntegerField('Координата по Y')

    class Meta:
        unique_together = [['plan', 'x', 'y']]
        verbose_name = 'Рабочее место'
        verbose_name_plural = 'Рабочие места'

    def __str__(self):
        return f'Рабочее место схемы {self.plan}'
    
    def clean(self) -> None:
        if self.x > self.plan.width:
            raise ValidationError(
                f'Координата рабочего места {self.x} '
                f'выходит за рамки ширины изображения ({self.plan.width})'
            )
        if self.y > self.plan.height:
            raise ValidationError(
                f'Координата рабочего места {self.y} '
                f'выходит за рамки высоты изображения ({self.plan.height})'
            )
        

@receiver(post_delete, sender=Plan)
def remove_img(sender, instance: Plan, **kwargs):
    if instance.img:
        if os.path.isfile(instance.img.path):
            os.remove(instance.img.path)


@receiver(pre_save, sender=Plan)
def remove_previous_img(sender, instance: Plan, **kwargs):
    if not instance.pk:
        return False
    try:
        previous_img = Plan.objects.get(pk=instance.pk).img
    except Plan.DoesNotExist:
        return False
    
    actual_img = instance.img
    if not previous_img == actual_img:
        if os.path.isfile(previous_img.path):
            os.remove(previous_img.path)
