# Generated by Django 3.2.5 on 2021-08-02 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do aluno')),
                ('profissao', models.CharField(max_length=200, verbose_name='Profissão do aluno')),
                ('ano_nascimento', models.PositiveSmallIntegerField()),
                ('ativo', models.BooleanField(default=True, verbose_name='O aluno está ativo')),
            ],
        ),
    ]