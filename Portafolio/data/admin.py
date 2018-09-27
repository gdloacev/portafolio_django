from django.contrib import admin
import data.models as models

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Project, ProjectAdmin)