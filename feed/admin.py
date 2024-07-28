from django.contrib import admin
from .models import Video, VideoTheme, Theme
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class VideoThemeInlineFormset(BaseInlineFormSet):
    def clean(self):
        has_selected_sections = False
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data.get('is_main'):
                has_selected_sections = True
                break
        if not has_selected_sections:
            raise ValidationError('Укажите основной раздел')
        main_section_count = 0
        for form in self.forms:
            if form.cleaned_data.get('DELETE'):
                continue
            if form.cleaned_data.get('is_main'):
                main_section_count += 1
        if main_section_count == 0:
            raise ValidationError('Укажите основной раздел!')
        elif main_section_count > 1:
            raise ValidationError('Основным может быть только один раздел')

        return super().clean()


class VideoThemeInline(admin.TabularInline):
    model = VideoTheme
    formset = VideoThemeInlineFormset
    extra = 3


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [VideoThemeInline]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']
