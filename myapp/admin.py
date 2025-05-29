from django.contrib import admin
from django.utils.html import format_html
from .models import PersonalInfo, EducationalProgram, Management, Classmate, PageContent, Student

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'show_photo')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('show_photo',)

    def show_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "Нет фото"
    show_photo.short_description = 'Фото'

@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_url', 'truncated_subjects')
    search_fields = ('name', 'subjects')
    list_filter = ('name',)

    def truncated_subjects(self, obj):
        return obj.subjects[:100] + '...' if len(obj.subjects) > 100 else obj.subjects
    truncated_subjects.short_description = 'Предметы'

@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email', 'show_photo')
    list_filter = ('role',)
    search_fields = ('full_name', 'email')
    readonly_fields = ('show_photo',)

    def show_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "Нет фото"
    show_photo.short_description = 'Фото'

@admin.register(Classmate)
class ClassmateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'show_photo')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('show_photo',)

    def show_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.photo.url)
        return "Нет фото"
    show_photo.short_description = 'Фото'

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('get_page_name_display', 'title', 'last_updated')
    list_filter = ('page_name',)
    search_fields = ('title', 'content')
    readonly_fields = ('last_updated',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('page_name', 'title')
        }),
        ('Содержание', {
            'fields': ('content',)
        }),
        ('Метаданные', {
            'fields': ('last_updated',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'educational_program', 'course', 'created_at')
    list_filter = ('course', 'educational_program')
    search_fields = ('full_name', 'educational_program')
    ordering = ('full_name', 'course')
    date_hierarchy = 'created_at'
    list_per_page = 20

    fieldsets = (
        ('Основная информация', {
            'fields': ('full_name', 'educational_program', 'course')
        }),
        ('Метаданные', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at',)

# Настройка внешнего вида админки
admin.site.site_header = 'Управление сайтом'
admin.site.site_title = 'Панель управления'
admin.site.index_title = 'Администрирование сайта'
