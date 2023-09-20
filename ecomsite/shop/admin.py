from django.contrib import admin
from .models import Products, Orders

# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Default Category'

    list_display = ('title', 'price', 'disount_price', 'category', 'description')
    search_fields = ('title', 'price')
    actions = ('change_category_to_default',)

    # fields = ('title', 'price')   Only this fields are viewable in admin section

    list_editable = ('price', 'disount_price', 'category')



admin.site.register(Products, ProductAdmin)
admin.site.register(Orders)
