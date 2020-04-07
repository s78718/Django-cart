from django.contrib import admin
from polls.models import Event,Guest


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']
    search_fields = ['name']    # 搜尋功能
    list_filter = ['status']    # 過濾器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event_id']
    list_display_links = ('realname', 'phone') # 顯示超連結
    search_fields = ['realname','phone']       # 搜尋功能
    list_filter = ['event_id']                 # 過濾器


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
