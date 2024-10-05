from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(SEO)
class SEOAdmin(admin.ModelAdmin):
    pass

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass

@admin.register(Block_UTP)
class Block_UTP(admin.ModelAdmin):
    pass

@admin.register(Example)
class Example(admin.ModelAdmin):
    pass

@admin.register(SRO)
class SRO(admin.ModelAdmin):
    pass


@admin.register(Stati)
class Stati(admin.ModelAdmin):
    pass