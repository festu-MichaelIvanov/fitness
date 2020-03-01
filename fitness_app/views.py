from rest_framework import viewsets

from fitness_app.serializers import ProgramSerializer
from fitness_app.models import Program


class ProgramViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Program view set
    """

    queryset = Program.objects.select_related('teacher_v2').all()
    serializer_class = ProgramSerializer
