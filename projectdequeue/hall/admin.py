from django.contrib import admin
from hall.models import Hall

class HallAdmin(admin.ModelAdmin):
	list_display=('hall_id','total_seats','total_seats_allocated')

admin.site.register(Hall,HallAdmin)
