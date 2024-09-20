from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answer, Summary, Award, Subject

# Create your views here.
def visualize_data(request):

    schools = School.objects.all()
    classes = Class.objects.all()
    assessment_areas = AssessmentArea.objects.all()
    students = Student.objects.all()
    answers = Answer.objects.all()
    summaries = Summary.objects.all()
    awards = Award.objects.all()
    subjects = Subject.objects.all()

    context = {
        'schools': schools,
        'classes': classes,
        'assessment_areas': assessment_areas,
        'students': students,
        'answers': answers,
        'summaries': summaries,
        'awards': awards,
        'subjects': subjects,
    }

    return render(request, 'tables.html', context)
