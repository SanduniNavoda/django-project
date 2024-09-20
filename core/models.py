from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100)

class Class(models.Model):
    class_name = models.CharField(max_length=100)

class AssessmentArea(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    full_name = models.CharField(max_length=100)

class Answer(models.Model):
    answer_text = models.TextField()

class Award(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_score = models.IntegerField()

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.BooleanField()
    sydney_percentile = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.BooleanField()
    student_score = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=100)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    correct_answer_id = models.IntegerField()
