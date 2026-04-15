from django.contrib import admin

from escola.models import Professor
from escola.models import Aluno
from escola.models import Curso
# Register your models here.
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Curso)

