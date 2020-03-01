from rest_framework import serializers

from fitness_app.models import Program, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    """
    Teacher serializer
    """

    class Meta:
        model = Teacher
        exclude = ('id',)


class ProgramSerializer(serializers.ModelSerializer):
    """
    Program serializer
    """

    teacher_v2 = TeacherSerializer()

    class Meta:
        model = Program
        exclude = ('id',)
