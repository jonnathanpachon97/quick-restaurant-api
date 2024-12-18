# Generated by Django 5.1.4 on 2024-12-13 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('status', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=11, max_digits=21)),
                ('longitude', models.DecimalField(decimal_places=11, max_digits=21)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activate', models.BooleanField(default=True)),
            ],
        ),
    ]
