# Generated by Django 5.0.3 on 2024-03-23 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_decks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carddeck',
            name='set_of_cards',
        ),
    ]