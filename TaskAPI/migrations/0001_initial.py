# Generated by Django 5.1.7 on 2025-03-31 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('E', 'Em andamento'), ('C', 'Concluída')], default='P', max_length=1)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('data_conclusao', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
                'ordering': ['-data_criacao'],
            },
        ),
    ]
