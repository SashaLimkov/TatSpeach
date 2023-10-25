from django.contrib import admin
from .models import TelegramUser, Language, Translate, Text

class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ("telegram_id","full_name", "count_of_sintez_tat", "count_of_sintez_rus", "count_of_detect_tat", "count_of_detect_rus", "selected_language")
    list_display_links = ("full_name", )
    search_fields = ("full_name", "telegram_id",)


class TranslatesAdmin(admin.ModelAdmin):
    list_display = ("key", "language", "translate")
    list_display_links = ("translate", )
    raw_id_fields = ("key", "language")
    search_fields = ("Translate",)
    list_filter = ("language",)

class TranslatesInline(admin.StackedInline):
    model = Translate
    fields = ["key", "language", "translate"]
    show_change_link = True
    extra = 0


class TextAdmin(admin.ModelAdmin):
    inlines = [TranslatesInline]


admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Language)
admin.site.register(Translate, TranslatesAdmin)
admin.site.register(Text, TextAdmin)
# Register your models here.
