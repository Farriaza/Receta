from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "recetas"

urlpatterns = [
    path("", views.index, name="index"),
    path("registro/", views.registro, name="registro"),
    path("login/", views.iniciar_sesion, name="login"),
    path("inicio/", views.inicio, name="inicio"),
    path("perfil/", views.perfil, name="perfil"),
    path("cerrar-sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
    path("subir-receta/", views.subir_receta, name="subir_receta"),
    path("recetas/", views.recetas, name="recetas"),
     path("recetas/panel/", views.panel_recetas, name="panel_recetas"),
    path("recetas/editar/<int:receta_id>/", views.editar_receta, name="editar_receta"),
    



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
