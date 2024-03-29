# Generated by Django 3.0.6 on 2020-05-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('trecho_id', models.IntegerField(null=True)),
                ('resposta', models.CharField(max_length=1)),
                ('data_avaliacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trechos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_endereco', models.CharField(max_length=100)),
                ('inicio', models.IntegerField()),
                ('fim', models.IntegerField()),
            ],
        ),
    ]
