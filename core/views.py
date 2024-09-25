from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answer, Summary, Award, Subject

# Create your views here.
def visualize_data(request):

    schools = School.get_all_schools(School)
    classes = Class.get_all_classes()
    assessment_areas = AssessmentArea.get_all_assessments()
    students = Student.get_all_students()
    answers = Answer.get_all_answers()
    awards = Award.get_all_awards()

    subject_scores = Subject.get_all_subjects()
    subjects = Subject.get_subject_score(subject_scores)

    summaries = Summary.objects.all()

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
