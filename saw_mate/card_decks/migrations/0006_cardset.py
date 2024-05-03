# Generated by Django 5.0.3 on 2024-04-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_decks', '0005_delete_cardset'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Набор карт')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Количество')),
                ('cards', models.ManyToManyField(null=True, related_name='cards', to='card_decks.carddeck', verbose_name='Карточки в наборе')),
            ],
            options={
                'verbose_name': 'Набор карт',
                'verbose_name_plural': 'Наборы карт',
                'db_table': 'cardset',
            },
        ),
    ]
