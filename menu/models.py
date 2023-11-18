from django.db import models

from user.models import NULLABLE
# Анита

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(**NULLABLE)
    soup = models.ManyToManyField('Soup', related_name='soup')
    main = models.ManyToManyField('Main', related_name='main')
    dessert = models.ManyToManyField('Dessert', related_name='dessert')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = 'меню'


class Soup(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    ingredients = models.CharField(max_length=100, verbose_name='ингредиенты')
    allergens = models.CharField(max_length=100, **NULLABLE)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'суп'
        verbose_name_plural = 'супы'


class Main(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    ingredients = models.CharField(max_length=100, verbose_name='ингредиенты')
    allergens = models.CharField(max_length=100, **NULLABLE)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'главное'
        verbose_name_plural = 'главные'


class Dessert(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    ingredients = models.CharField(max_length=100, verbose_name='ингредиенты')
    allergens = models.CharField(max_length=100, **NULLABLE)
    description = models.TextField(**NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'десерт'
        verbose_name_plural = 'десерты'
