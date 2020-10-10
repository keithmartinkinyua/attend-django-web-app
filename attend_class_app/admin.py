from django.contrib import admin
from .models import Units

admin.site.register(Units)


'''@admin.register(Units)
class Unitts(admin.ModelAdmin): 
    list_display = ('UnitName', 'Lecturer', 'UnitTopics')
    list_filter = ('UnitName', 'Lecturer', 'UnitTopics')  
    ordering = ('id') '''