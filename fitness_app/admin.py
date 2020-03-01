from django.contrib import admin

from fitness_app.models import Program, Teacher


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'place', 'teacher', 'start_time', 'end_time',
                    'weekDay', 'availability', 'pay', 'appointment']
    list_filter = ['availability', 'pay', 'appointment']
    raw_id_fields = ['teacher_v2']
    search_fields = ['name', 'description', 'place', 'teacher']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'name', 'position']
    search_fields = ['short_name', 'name', 'position']
