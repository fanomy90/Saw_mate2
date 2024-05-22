# Generated by Django 5.0.3 on 2024-03-22 23:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('session_key', models.CharField(blank=True, max_length=32, null=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.products', verbose_name='Товар')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Колода карт',
                'verbose_name_plural': 'Колоды карт',
                'db_table': 'carddeck',
            },
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Набор карт')),
                ('cards_in_set', models.ManyToManyField(related_name='cards_in_set', to='card_decks.carddeck', verbose_name='Карточки в наборе')),
            ],
            options={
                'verbose_name': 'Набор карт',
                'verbose_name_plural': 'Наборы карт',
                'db_table': 'cardset',
            },
        ),
        migrations.AddField(
            model_name='carddeck',
            name='set_of_cards',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card_decks.cardset', verbose_name='Набор карт'),
        ),
    ]