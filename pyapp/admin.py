from django.contrib import admin
from django.contrib.auth.models import Permission
from django.utils.html import mark_safe
from .models import User, Category, Course, Lesson, Tag

class LessonTagInlineAdmin(admin.TabularInline):
    model = Lesson.tag.through

class LessonAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created_date', 'active', 'course']
    search_fields = ['subject', 'course__subject']
    list_filter = ['subject', 'course__subject']
    readonly_fields = ['thumbnail']
    inlines = (LessonTagInlineAdmin,)

    def thumbnail(self, obj):
        if (obj):
            return mark_safe('''
                <img src="/static/{img_url}" width="120" alt="{img_alt}" />
            '''.format(img_url=obj.image.name, img_alt=obj.subject))


class LessonInlineAdmin(admin.StackedInline):
    model = Lesson
    pk_name = 'course'


class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInlineAdmin,)


# Register your models here.
admin.site.register(Permission)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
