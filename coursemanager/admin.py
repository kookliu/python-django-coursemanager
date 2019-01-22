from django.contrib import admin
from coursemanager.models import Course, Venue, Presentation, Attendee, Trainer, CostCode, Environment, CourseMaterial, Report

class CourseMaterialInline(admin.StackedInline):
    model = CourseMaterial
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','duration','cost','min_attendees', 'max_attendees')

    inlines = [CourseMaterialInline]
     
class VenueAdmin(admin.ModelAdmin):
    list_display = ('room', 'maxdelegates')
    
class AttendeeInline(admin.StackedInline):
    model = Attendee
    extra = 1
    
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('course', 'startdate', 'starttime', 'status', 'venue', 'trainer', 'num_attendees')
    list_filter = ['startdate', 'status']
    
    inlines = [AttendeeInline]
    
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('emailaddress', 'presentation', 'firstname', 'lastname', 'extension', 'attendancestatus')
    search_fields = ('emailaddress', 'firstname', 'lastname')
 
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('emailaddress', 'firstname', 'lastname','extension')
    
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ('name','description','reference')
    
class CostCodeAdmin(admin.ModelAdmin):
     list_display = ()

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
admin.site.register(Report, ReportAdmin)


