from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VRegistro, cerrar_sesion, iniciar_sesion, monitoreo

from django.contrib.auth import views as auth_views
#,reconocimiento_facial
urlpatterns = [
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_sesion"),
    path('iniciar_sesion', iniciar_sesion, name="Iniciar_sesion"),
    path('monitoreo', monitoreo, name="Monitoreo"),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)