from django.contrib import admin

from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'done')
    readonly_fields = ('created_at', )


admin.site.register(ToDo, ToDoAdmin)
