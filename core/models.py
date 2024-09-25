from django.db import models
from django.db.models import Avg

# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)

    @classmethod
    def get_all_schools(cls):
        unique_school = set()
        for school in cls.objects.all():
            unique_school.add((school.id, school.school_name))
        return list(unique_school)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=50, db_column='class')

    @classmethod
    def get_all_classes(cls):
        unique_class = set()
        for classes in cls.objects.all():
            unique_class.add((classes.id, classes.class_name))
        return list(unique_class)

class AssessmentArea(models.Model):
    id = models.AutoField(primary_key=True)
    assessment_areas = models.CharField(max_length=100)

    @classmethod
    def get_all_assessments(cls):
        unique_assessment = set()
        for assessmentArea in cls.objects.all():
            unique_assessment.add((assessmentArea.id, assessmentArea.assessment_areas))
        return list(unique_assessment)

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    @classmethod
    def get_all_students(cls):
        unique_names = set() # Use a set to avoid duplicates
        for student in cls.objects.all():
            full_name = student.full_name()
            unique_names.add([student.id, full_name])
        return list(unique_names)

            
    
    def __str__(self):
        return self.full_name()
    
class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=1)

    @classmethod
    def get_all_answers(cls):
        unique_answers = set()
        for answer in cls.objects.all():
            unique_answers.add((answer.id, answer.answer))
        return list(unique_answers)

class Award(models.Model):
    id = models.AutoField(primary_key=True)
    award = models.CharField(max_length=100)

    @classmethod
    def get_all_awards(cls):
        unique_awards = set()
        for award in cls.object.all():
            unique_awards.add((award.id, award.award))
    

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    average_score = models.DecimalField(max_digits=5, decimal_places=2)
    

    @classmethod
    def get_all_subjects(cls):
        subject_scores = []
        for subject in cls.object.all():
            subject_scores.append([subject.subject_name, subject.average_score])
        return subject_scores


    def get_subject_score(subject_scores):
        subject_score_dict = {}

        for score in subject_scores:
            count = 0
            subject_name = score[0]
            subject_avg = score[1]

            if subject_name in subject_score_dict:
                subject_score_dict[subject_name]['total_score'] += subject_avg
                subject_score_dict[subject_name]['count'] += 1
            else:
                subject_score_dict[subject_name] = {
                    'total_score': subject_avg,
                    'count': 1
                }

        final_subject_scores = []
        for subject_name, data in subject_score_dict.items():
            average_score = data['total_score'] / data['count']
            final_subject_scores.append([subject_name, average_score])
        
        return final_subject_scores


            


class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    average_sydney_participant = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    average_sydney_percentile = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.DecimalField(max_digits=5, decimal_places=2)
    correct_answer = models.CharField(max_length=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.IntegerField()
    student_score = models.DecimalField(max_digits=5, decimal_places=2)
    subject_id = models.IntegerField()
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=50)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
