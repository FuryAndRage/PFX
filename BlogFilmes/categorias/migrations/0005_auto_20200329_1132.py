# Generated by Django 3.0.4 on 2020-03-29 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0003_remove_filmes_categorias_filme'),
        ('categorias', '0004_auto_20200329_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='nome_filme',
        ),
        migrations.AddField(
            model_name='categoria',
            name='nome_filme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filmes.Filmes'),
        ),
    ]
