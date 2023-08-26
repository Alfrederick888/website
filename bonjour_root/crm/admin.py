from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm

class Coment(admin.StackedInline):
    model = ComentCrm
    fields = ('coment_data', 'coment_text')
    readonly_fields = ('coment_data',)
    extra = 0

class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'status', 'name', 'phone', 'data')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'phone', 'data')
    list_filter = ('status',)
    list_editable = ('status', 'phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'status', 'data', 'name', 'phone')
    readonly_fields = ('id', 'data')
    inlines = [Coment,]

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
