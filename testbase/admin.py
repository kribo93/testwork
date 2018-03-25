from django.contrib import admin
from testbase.models import Student, Group, Model_Log
from django.utils.html import format_html
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'date_of_birth', 'card_number', 'in_group']

class StudentInline(admin.TabularInline):
    model = Student

class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course_leader']
    inlines = [StudentInline]

class ModelLogAdmin(admin.ModelAdmin):
    model = Model_Log
    list_display = ['model_name', 'object_name', 'action', 'datetime']

    def show_url(self, obj):
        return format_html("%s", obj.object_name)

    show_url.allow_tags = True

admin.site.register(Student, StudentAdmin)
admin.site.register(Group, StudyGroupAdmin)
admin.site.register(Model_Log, ModelLogAdmin)

