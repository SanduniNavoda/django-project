from django.contrib import admin
from .models import School, Class, AssessmentArea, Student, Answer, Summary, Award, Subject

# Register your models here.

admin.site.register(School)
admin.site.register(Class)
admin.site.register(AssessmentArea)
admin.site.register(Student)
admin.site.register(Answer)
admin.site.register(Summary)
admin.site.register(Award)
admin.site.register(Subject)