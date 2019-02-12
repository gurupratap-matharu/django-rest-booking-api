from django.contrib import admin
from api.models import Sport, Match, Market, Selection


class SelectionInline(admin.StackedInline):
    model = Selection
    extra = 3


class MarketAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,        {'fields': ['name']}),
        ('Sport',     {'fields': ['sport']}),
    ]
    inlines = [SelectionInline]

class MatchAdmin(admin.ModelAdmin):
    fields = ['name', 'startTime', 'sport', 'market']


admin.site.register(Market, MarketAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Sport)
admin.site.register(Selection)
