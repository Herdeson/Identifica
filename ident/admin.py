# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Individuo

# Register your models here.

class ControleAdmin(admin.ModelAdmin):
    #exclude = ('modificador','ip_host', 'nome_host')
    list_per_page = 20

    ''' 
    Montar o formulario
    dar um exclude nos fields escolhidos
    verificar se a funcao de permissao por fields foi setada no admin
    caso n seja exclui os fields
    '''
   
    
    def get_form(self, request, obj=None, **kwargs):
            if hasattr(self, 'field_permissions'):
                user = request.user

                for _field in self.opts.fields:

                    perm = self.field_permissions.get(_field.name)

                    if perm and not user.has_perm(perm):

                        if self.exclude:
                            #print("1")
                            print(self.exclude)
                            self.exclude.append(_field.name)
                            #self.exclude.append('modificador')
                            self.exclude.append('ip_host')

                        else:
                            self.exclude = [_field.name]
            else:
                #exclude = ('modificador','ip_host')
                self.exclude = ['ip_host',]
            return super(ControleAdmin, self).get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        obj.modificador = request.user
        obj.ip_host = request.META.get('REMOTE_ADDR','')
        #obj.nome_host = request.META.get('REMOTE_HOST','')        
        obj.save()

class IndividuoAdmin(ControleAdmin):
    pass




admin.site.register(Individuo , IndividuoAdmin)
