from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Perfil, Receta, Categoria
from django.shortcuts import render, redirect, get_object_or_404


User = get_user_model()


# =========================
# INDEX / LANDING
# =========================
@ensure_csrf_cookie
def index(request):
    recipes = Receta.objects.all()
    categories = Categoria.objects.all()

    return render(request, "recetas/index.html", {
        "recipes": recipes,
        "categories": categories,
    })


# =========================
# REGISTRO
# =========================
def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect("recetas:index")

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect("recetas:index")

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo ya está registrado")
            return redirect("recetas:index")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.first_name = full_name
        user.save()

        # 🔹 Crear perfil automáticamente
        Perfil.objects.get_or_create(user=user)

        messages.success(request, "Cuenta creada correctamente")
        return redirect("recetas:index")

    return redirect("recetas:index")


# =========================
# LOGIN
# =========================
def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ✅ CORRECTO
            Perfil.objects.get_or_create(user=user)

            return redirect("recetas:inicio")

        messages.error(request, "Usuario o contraseña incorrectos")
        return redirect("recetas:index")

    return redirect("recetas:index")


# =========================
# INICIO (DASHBOARD)
# =========================
@login_required
def inicio(request):
    recetas = Receta.objects.filter(autor=request.user)

    return render(request, "recetas/inicio.html", {
        "recetas": recetas
    })

# =========================
# PERFIL
# =========================
@login_required(login_url="recetas:index")
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        request.user.username = request.POST.get("username")
        request.user.email = request.POST.get("email")
        request.user.save()

        perfil.bio = request.POST.get("bio")
        perfil.especialidad = request.POST.get("especialidad")
        perfil.social_link = request.POST.get("social_link")

        if "foto" in request.FILES:
            perfil.foto = request.FILES["foto"]

        perfil.save()
        messages.success(request, "Perfil actualizado")

        return redirect("recetas:perfil")

    return render(request, "recetas/perfil.html", {
        "perfil": perfil
    })

@login_required(login_url="recetas:login")
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name", "")
        request.user.last_name = request.POST.get("last_name", "")
        request.user.email = request.POST.get("email", "")
        request.user.save()

        perfil.bio = request.POST.get("bio")
        perfil.especialidad = request.POST.get("especialidad")

        if "foto" in request.FILES:
            perfil.foto = request.FILES["foto"]

        perfil.save()
        messages.success(request, "Perfil actualizado correctamente")
        return redirect("recetas:perfil")

    return render(request, "recetas/perfil_editar.html", {
        "perfil": perfil
    })

# =========================
# LOGOUT
# =========================
def cerrar_sesion(request):
    logout(request)
    return redirect("recetas:index")

@login_required
def subir_receta(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        ingredientes = request.POST.get("ingredientes")

        # El form envía "instrucciones"
        pasos = request.POST.get("instrucciones")

        categoria_id = request.POST.get("categoria")

        # Imagen: archivo o URL
        imagen_archivo = request.FILES.get("imagen_archivo")
        imagen_url = request.POST.get("imagen_url")

        categoria = Categoria.objects.get(id=categoria_id)

        # 🔥 AQUÍ ESTABA EL ERROR
        receta = Receta.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            ingredientes=ingredientes,
            pasos=pasos,
            categoria=categoria,
            autor=request.user     # ✅ CLAVE
        )

        # Asignar imagen correctamente
        if imagen_archivo:
            receta.imagen = imagen_archivo
        elif imagen_url:
            receta.imagen = imagen_url

        receta.save()

        return redirect("recetas:inicio")

    categorias = Categoria.objects.all()
    return render(request, "recetas/subir_receta.html", {
        "categorias": categorias
    })

@login_required
def recetas(request):
    todas_recetas = Receta.objects.all().select_related("autor", "categoria")
    return render(request, "recetas/recetas.html", {"recetas": todas_recetas})


@login_required
def panel_recetas(request):
    # Traemos solo las recetas del usuario
    mis_recetas = Receta.objects.filter(autor=request.user)

    return render(request, "recetas/panel_recetas.html", {
        "recetas": mis_recetas
    })

# Editar receta
@login_required
def editar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id, autor=request.user)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        receta.titulo = request.POST.get("titulo")
        receta.descripcion = request.POST.get("descripcion")
        receta.ingredientes = request.POST.get("ingredientes")
        receta.pasos = request.POST.get("pasos")

        categoria_id = request.POST.get("categoria")
        receta.categoria = Categoria.objects.get(id=categoria_id)

        if "imagen_archivo" in request.FILES:
            receta.imagen = request.FILES["imagen_archivo"]
        elif request.POST.get("imagen_url"):
            receta.imagen = request.POST.get("imagen_url")

        receta.save()
        messages.success(request, "Receta actualizada correctamente")
        return redirect("recetas:panel_recetas")

    return render(request, "recetas/editar_receta.html", {
        "receta": receta,
        "categorias": categorias
    })

