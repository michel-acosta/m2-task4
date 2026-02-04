from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignaturaViewSet, NotaViewSet, notas_por_asignatura


router = DefaultRouter()
router.register(r'notas', NotaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/notas/asignatura/<int:asignatura_id>/', notas_por_asignatura),
]

router.register(r'asignaturas', AsignaturaViewSet)
