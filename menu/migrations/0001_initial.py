# Generated by Django 4.2.7 on 2023-11-15 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('ingredients', models.CharField(max_length=100, verbose_name='ингредиенты')),
                ('allergens', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'десерт',
                'verbose_name_plural': 'десерты',
            },
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('ingredients', models.CharField(max_length=100, verbose_name='ингредиенты')),
                ('allergens', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'главное',
                'verbose_name_plural': 'главные',
            },
        ),
        migrations.CreateModel(
            name='Soup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('ingredients', models.CharField(max_length=100, verbose_name='ингредиенты')),
                ('allergens', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'суп',
                'verbose_name_plural': 'супы',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('dessert', models.ManyToManyField(related_name='dessert', to='menu.dessert')),
                ('main', models.ManyToManyField(related_name='main', to='menu.main')),
                ('soup', models.ManyToManyField(related_name='soup', to='menu.soup')),
            ],
            options={
                'verbose_name': 'меню',
                'verbose_name_plural': 'меню',
            },
        ),
    ]
