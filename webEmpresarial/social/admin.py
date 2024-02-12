from django.contrib import admin

# Register your models here.


from .models import Links

class LinksAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Links, LinksAdmin)

