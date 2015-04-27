# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individuo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Cria\xe7\xe3o')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Data da Modifica\xe7\xe3o')),
                ('status', models.BooleanField()),
                ('ip_host', models.CharField(max_length=15, null=True, blank=True)),
                ('foto', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('nome', models.CharField(max_length=200)),
                ('alcunha', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1, choices=[(b'M', b'MASCULINO'), (b'F', b'FEMININO')])),
                ('natural', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tatuagens',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Cria\xe7\xe3o')),
                ('dataModificacao', models.DateTimeField(auto_now=True, verbose_name='Data da Modifica\xe7\xe3o')),
                ('status', models.BooleanField()),
                ('ip_host', models.CharField(max_length=15, null=True, blank=True)),
                ('local', models.CharField(max_length=1, verbose_name=b'Local da Tatuagem', choices=[(b'C', b'CABE\xc3\x87A'), (b'T', b'TRONCO'), (b'S', b'MEMBROS SUPERIORES'), (b'I', b'MEMBROS INFERIORES')])),
                ('tatuagem', models.ImageField(upload_to=b'')),
                ('individuo', models.ForeignKey(verbose_name=b'Individuo', to='ident.Individuo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
