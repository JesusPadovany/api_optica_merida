from django.conf.urls import url
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from lentes import views 



router = DefaultRouter()
router.register(r'users', views.UsuarioViewSet, basename='users')
 
urlpatterns = [ 
    path('', include(router.urls)),
    url(r'^api/lentes$', views.lentes_list),
    url(r'^api/lentes/(?P<pk>[0-9]+)$', views.lentes_detail),

    url(r'^api/lente_tipos$', views.lente_tipos_list),
    url(r'^api/lente_tipos/(?P<pk>[0-9]+)$', views.lente_tipos_detail),

    url(r'^api/marcas$', views.marcas_list),
    url(r'^api/marcas/(?P<pk>[0-9]+)$', views.marcas_detail),

    url(r'^api/usuarios$', views.usuarios_list),
    url(r'^api/usuarios/(?P<pk>[0-9]+)$', views.usuarios_detail),

    url(r'^api/compras$', views.compras_list),
    url(r'^api/compras/(?P<pk>[0-9]+)$', views.compras_detail),

]