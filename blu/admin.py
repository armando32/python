from django.contrib import admin
from .models import verification
# Register your models here.

class zap(admin.ModelAdmin):
    list_display = ('ver_tok','ver','val_until','pay','last_mod',)

admin.site.register(verification,zap)
