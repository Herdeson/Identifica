# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, FormView

from .models import Individuo

from .forms import IndividuoForm
from ident.forms import TatuagemFormSet

# Create your views here.

def submit_tatuagem(request):
    if request.POST:
        
        form = IndividuoForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            tatuagem_formset = TatuagemFormSet(request.POST, instance=recipe)
            
            if tatuagem_formset.is_valid():
                recipe.save()
                tatuagem_formset.save()
                
                return HttpResponseRedirect('/identifica/')
            
    else:
        form = IndividuoForm()
        tatuagem_formset = TatuagemFormSet(instance = Individuo())
        
    return render(request, 'ident/formset.html' , {
                        "form": form,
                        "tatuagem_formset": tatuagem_formset,}
                        )
    



def teste(request):
    return render(request,'ident/index.html')

class IndexView(ListView):
    model = Individuo
    template_name = 'ident/index.html'

    def get_queryset(self):
        return Individuo.objects.order_by('-dataModificacao')

class IndividuoCreate(CreateView):
    model = Individuo
    fields = ['nome' , 'alcunha', 'sexo' , 'natural' , 'foto' , 'status']
    success_url = "/identifica/"

'''
class IndividuoForm(FormView):
    template_name = 'individuo_form.html'
    form_class = IndividuoForm
    success_url = "/identifica/"
'''


