# Generated by Django 2.2 on 2019-04-03 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produtos.Categoria'),
        ),
    ]
