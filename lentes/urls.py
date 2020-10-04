from django.conf.urls import url 
from lentes import views 
 
urlpatterns = [ 
    url(r'^api/lentes$', views.lentes_list),
    url(r'^api/lentes/(?P<pk>[0-9]+)$', views.lentes_detail),

    url(r'^api/lente_tipos$', views.lente_tipos_list),
    url(r'^api/lente_tipos/(?P<pk>[0-9]+)$', views.lente_tipos_detail),

    url(r'^api/marcas$', views.marcas_list),
    url(r'^api/marcas/(?P<pk>[0-9]+)$', views.marcas_detail),
]