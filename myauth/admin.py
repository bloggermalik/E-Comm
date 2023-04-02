from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import *


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    list_display = ('first_name','phone', 'email',  'last_name', 'is_staff')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',)
    list_display_links = ('first_name', 'phone')

    def phone_number(self, obj):
        phone = obj.phone
        url = reverse('admin:view_on_site', args=[phone])
        return format_html('<a href="{}">{}</a>', url, phone)


admin.site.register(get_user_model(), CustomUserAdmin)


class iteminline(admin.StackedInline):
    model = OrderItem
    extra = 0

class myOrder(admin.ModelAdmin):
    inlines = [iteminline]
    list_display =[ '__str__','status' ,'created_at']

class myOrderItem(admin.ModelAdmin):
    list_display =['order','product']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone', 'city', 'created_at')


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order, myOrder)
admin.site.register(OrderItem, myOrderItem)

