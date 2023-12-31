# Generated by Django 4.2.2 on 2023-07-26 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_usuariopersonalizado'),
    ]

    operations = [
        migrations.CreateModel(
            name='datosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinero', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
