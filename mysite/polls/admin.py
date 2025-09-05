from django.contrib import admin
from .models import Question, Choice

# Clase Inline para agregar Choices dentro de Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Muestra 3 campos vacíos por defecto

# Personalización del admin de Question
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Fecha de publicación", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]  # <- Esto es lo que permite cargar las opciones

# Registrar modelos en el admin
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)



