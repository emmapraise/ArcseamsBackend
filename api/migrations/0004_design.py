# Generated by Django 4.1.4 on 2022-12-26 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('images', models.ManyToManyField(to='api.image')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.measurement')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]