from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import FormularioUsuario
from django.utils.datastructures import MultiValueDictKeyError
from usuario.models import Usuario
from django import forms
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
# Create your views here.
class VRegistro(View):
    def get(self, request):
        form=CustomUserCreationForm()
        custom_form=FormularioUsuario()
        return render(request,"registro/registro.html",{"form":form,"custom_form":custom_form})
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        custom_form = FormularioUsuario(request.POST, request.FILES)

        if form.is_valid() and custom_form.is_valid():
            usuario = form.save()
            usuarioapp = custom_form.save(commit=False)
            if 'imagen' in request.FILES:
                usuario.imagen = request.FILES['imagen']
            usuarioapp.user = usuario
            usuarioapp.save()
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, "registro/registro.html", {"form": form, "custom_form": custom_form})


class VRegistro2(View):
    def get(self, request):
        form=CustomUserCreationForm()
        custom_form=FormularioUsuario()
        return render(request,"registro/registro.html",{"form":form,"custom_form":custom_form})
    
    def post(self,request):
        form=CustomUserCreationForm(request.POST)
        custom_form=FormularioUsuario(request.POST, request.FILES)


    
        if form.is_valid() and custom_form.is_valid():
            usuario=form.save()
            usuarioapp= custom_form.save(commit=False)
            usuario.imagen = request.FILES['imagen']
            usuarioapp.user = usuario
            usuarioapp.save()
            #addFace(request.POST['dpi'])
            login(request, usuario)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            
            return render(request,"registro/registro.html",{"form":form,"custom_form":custom_form})
        

def iniciar_sesion(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario=authenticate(username=username,password=password)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request,"Las credenciales ingresadas no coinciden con ningún usuario")
        else:
            messages.error(request,"Se ha ingresado información incorrecta")
            
    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})

class CustomUserCreationForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 12:
            raise forms.ValidationError("La contraseña debe tener al menos 12 caracteres.")
        if not re.search(r'[A-Z]', password1):
            raise forms.ValidationError("La contraseña debe contener al menos una mayúscula.")
        if not re.search(r'\d', password1):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[\W_]', password1):
            raise forms.ValidationError("La contraseña debe contener al menos un símbolo.")
        return password1

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')