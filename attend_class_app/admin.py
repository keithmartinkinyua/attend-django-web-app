from django.contrib import admin
from .models import Units, Lesson, Class

admin.site.register(Units)
admin.site.register(Lesson)
admin.site.register(Class)

'''@admin.register(Units)
class Unitts(admin.ModelAdmin): 
    list_display = ('UnitName', 'Lecturer', 'UnitTopics')
    list_filter = ('UnitName', 'Lecturer', 'UnitTopics')  
    ordering = ('id') '''