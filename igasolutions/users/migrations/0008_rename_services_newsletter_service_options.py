# Generated by Django 4.2.2 on 2023-06-12 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_newsletter_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='services',
            new_name='service_options',
        ),
    ]
