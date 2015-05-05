from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^individuo/add/$', views.IndividuoCreate.as_view(), name='individuo_add'),
    #url(r'^individuo/form/$', views.submit_tatuagem , name='formsets'),

   
]