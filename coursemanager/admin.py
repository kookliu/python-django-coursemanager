from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from coursemanager.models import Course, Venue, Presentation, Attendee, Trainer, CostCode, Environment, CourseMaterial, Report

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportMixin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter, RelatedOnlyDropdownFilter, AllValuesFieldListFilter
)

###
# Import Export resources
#####
class PresentationResource(resources.ModelResource):

    class Meta:
        model = Presentation
        fields = ('course__title', 'startdate', 'starttime', 'trainer__emailaddress', 'venue__room', 'status', 'num_attendees')

###
# Admin forms
####
class CourseMaterialInline(admin.StackedInline):
    model = CourseMaterial
    extra = 1

COURSES = [(course.id, course.title) for course in Course.objects.all()]
COURSES.insert(0, ('', '----'))

VENUES  = [(venue.id, venue.address) for venue in Venue.objects.all()]
VENUES.insert(0, ('', '----'))

TRAINERS  = [(trainer.id, f"{trainer.firstname} {trainer.lastname}") for trainer in Trainer.objects.all()]
TRAINERS.insert(0, ('', '----'))

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','duration','cost','min_attendees', 'max_attendees')

    inlines = [CourseMaterialInline]

class VenueAdmin(admin.ModelAdmin):
    list_display = ('room', 'maxdelegates')
    
class AttendeeInline(admin.StackedInline):
    model = Attendee
    extra = 1

######
# Presentations
###
class PresentationAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PresentationAdminForm, self).__init__(*args, **kwargs)
        self.fields['course'].choices=COURSES
        # self.fields['trainer'].choices = TRAINERS
        self.fields['venue'].choices = VENUES


class PresentationAdmin(ImportExportModelAdmin):
    list_display = ('course', 'startdate', 'starttime', 'status', 'venue', 'num_attendees', 'viable', 'trainer')

    list_filter = ['startdate',
                   ('status', ChoiceDropdownFilter),
                   ('course', RelatedDropdownFilter),
                   ('trainer', RelatedDropdownFilter)
                   ]
    actions = []

    resource_class = PresentationResource

    def viable(self, obj):
        return mark_safe(obj.attendee_check())

    viable.short_description = 'Course viability'

    form = PresentationAdminForm
    inlines = [AttendeeInline]

class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('emailaddress', 'course', 'start_date', 'firstname', 'lastname', 'extension', 'attendancestatus')
    search_fields = ('emailaddress', 'firstname', 'lastname')

    def course(self, obj):
        return obj.presentation.course.title

    def start_date(self, obj):
        return obj.presentation.startdate

class TrainerAdmin(admin.ModelAdmin):
    list_display = ('emailaddress', 'firstname', 'lastname','extension',
                    'trd_week', 'trd_month',
                    'ded_week', 'ded_month')
    
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name','description','reference')
    
class CostCodeAdmin(admin.ModelAdmin):
     list_display = ('code', 'title')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('sortorder','name', 'description')
    ordering = ['sortorder']

admin.site.register(Course, CourseAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Presentation, PresentationAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(CostCode, CostCodeAdmin)
# admin.site.register(Report, ReportAdmin)

admin.site.site_header = 'Coursemanager TMS'
admin.site.site_title = 'Coursemanager TMS'

