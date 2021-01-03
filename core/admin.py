from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, Coupon, Carrousel, Category, Refund, Address, UserProfile


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ref_code', 'ordered', 'being_delivered',
                    'received', 'refund_requested', 'refund_granted', 'billing_address', 'shipping_address', 'payment', 'coupon']
    list_display_links = ['user', 'billing_address',
                          'shipping_address', 'payment', 'coupon']
    list_filter = ['user', 'ordered', 'being_delivered',
                   'received', 'refund_requested', 'refund_granted']
    search_fields = ['user__username', 'ref_code']
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'apartment_address',
                    'country', 'zip', 'address_type', 'default']
    list_filter = ['user', 'address_type', 'default', 'country']
    search_fields = ['user__username',
                     'street_address', 'apartment_address', 'zip']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category', 'slug']
    list_filter = ['category']
    list_display_links = ['title', 'category']
    search_fields = ['title', 'subtitle', 'slug']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'active']
    search_fields = ['name']


admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Carrousel)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)