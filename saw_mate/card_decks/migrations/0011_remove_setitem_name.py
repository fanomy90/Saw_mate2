# Generated by Django 5.0.3 on 2024-04-04 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_decks', '0010_setitem_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setitem',
            name='name',
        ),
    ]
