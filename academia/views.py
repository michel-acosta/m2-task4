from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import QuerySet

from .models import Asignatura, Nota
from .serializers import NotaSerializer, AsignaturaSerializer
from .permissions import SoloProfesoresEscritura

class NotaViewSet(ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [SoloProfesoresEscritura]

    def get_queryset(self):  # type: ignore[override]
        user = self.request.user

        if user.groups.filter(name='Profesores').exists():
            return Nota.objects.all()

        return Nota.objects.filter(alumno=user)

class AsignaturaViewSet(ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer
    permission_classes = [SoloProfesoresEscritura]

@api_view(['GET'])
def notas_por_asignatura(request, asignatura_id):
    notas = Nota.objects.filter(asignatura_id=asignatura_id)
    serializer = NotaSerializer(notas, many=True)
    return Response(serializer.data)

class AsignaturaListView(ListView):
    model = Asignatura

class AsignaturaDetailView(DetailView):
    model = Asignatura

class AsignaturaCreateView(CreateView):
    model = Asignatura
    fields = '__all__'

class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    fields = '__all__'


class NotaListView(ListView):
    model = Nota

class NotaDetailView(DetailView):
    model = Nota

class NotaCreateView(CreateView):
    model = Nota
    fields = '__all__'

class NotaUpdateView(UpdateView):
    model = Nota
    fields = '__all__'
