# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from .models import Individuo

class IndividuoForm(ModelForm):
	class Meta:
		model = Individuo
        

