# -*- coding: utf-8 -*-
from django.db import models
# Create your models here.


SEXO=(('M', 'MASCULINO'),
          ('F', 'FEMININO'))

LOCAL_TATUAGEM=(('C', 'CABEÇA'),
                ('T','TRONCO'),
                ('S','MEMBROS SUPERIORES'),
                ('I','MEMBROS INFERIORES'))

class Controle(models.Model):
    
    dataCriacao = models.DateTimeField(auto_now_add=True,verbose_name = u"Data da Criação")
    dataModificacao = models.DateTimeField(auto_now=True,verbose_name = u"Data da Modificação")    
    status = models.BooleanField()
    #modificador = models.ForeignKey(User)
    ip_host = models.CharField(max_length=15, blank = True, null = True)
    #nome_host = models.CharField(max_length=20, blank = True, null = True)
    
    class Meta:
        abstract = True

class Individuo(Controle):
    foto = models.ImageField(blank=True, null=True)
    nome = models.CharField(max_length=200)
    alcunha = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices = SEXO )
    natural =  models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome




class Tatuagens(Controle):
    individuo = models.ForeignKey(Individuo, verbose_name="Individuo")
    local = models.CharField(max_length=1, choices = LOCAL_TATUAGEM, verbose_name="Local da Tatuagem")
    tatuagem = models.ImageField()


