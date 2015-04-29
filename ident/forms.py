# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Individuo
from django.forms.models import inlineformset_factory
from ident.models import Tatuagens

class IndividuoForm(ModelForm):
	class Meta:
		model = Individuo
		exclude = ['dataCriacao', 'dataModificacao', 'ip_host', ]
		#fields = [ 'foto', 'nome', 'alcunha' , 'sexo' , 'natural' , 'status']



MAX_TATUAGENS = 5

TatuagemFormSet = inlineformset_factory(Individuo,Tatuagens, form= IndividuoForm, can_delete=False, extra=MAX_TATUAGENS)