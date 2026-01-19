from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# =========================
# PERFIL DE USUARIO
# =========================
class Perfil(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil"
    )
    foto = models.ImageField(
        upload_to="perfiles/",
        default="perfiles/default.png",
        blank=True
    )
    bio = models.TextField(max_length=500, blank=True)
    especialidad = models.CharField(max_length=100, blank=True)
    social_link = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"


# =========================
# SIGNAL → CREA PERFIL AUTOMÁTICO
# =========================
@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


# =========================
# CATEGORÍAS
# =========================
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nombre


# =========================
# RECETAS
# =========================


class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    pasos = models.TextField()

    imagen = models.ImageField(
        upload_to="recetas/",
        blank=True,
        null=True
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

