import csv
import os
from django.core.management.base import BaseCommand
from core.models import School, Class, AssessmentArea, Student, Answer, Summary, Award, Subject

class Command(BaseCommand):
    help = 'Load data from CSV files into the database'


    def handle(self, *args, **kwargs):

        # Set the path to the data directory correctly
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        data_dir = os.path.join(base_dir, 'data')  # Adjusting to core/data directory


        
        csv_file_path = os.path.join(data_dir, 'Ganison_dataset_1.csv')
        if not os.path.exists(csv_file_path):
            print(f"File not found: {csv_file_path}")
            return
        

        # Load Schools
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                school_name = row['school_name']  # Adjust based on your CSV structure
                School.objects.get_or_create(name=school_name)


        # Load Classes
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                class_name = row['Class']
                Class.objects.get_or_create(class_name=class_name)

        # Load Assessment Areas
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                area_name = row['Assessment Areas']
                AssessmentArea.objects.get_or_create(name=area_name)

        # Load Students
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                full_name = f"{row['First Name']} {row['Last Name']}"
                Student.objects.get_or_create(full_name=full_name)

        # Load Answers
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                answer_text = row['Answers']
                Answer.objects.get_or_create(answer_text=answer_text)

        # Load Subjects
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                subject_name = row['Subject']
                subject_score = row['student_score']
                Subject.objects.get_or_create(subject_name=subject_name, subject_score=subject_score)

        # Load Summary
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                school = School.objects.get(name=row['school_name'])
                student = Student.objects.get(full_name=f"{row['First Name']} {row['Last Name']}")
                assessment_area = AssessmentArea.objects.get(name=row['Assessment Areas'])
                student_class = Class.objects.get(class_name=row['Class'])
                award = Award.objects.get(name=row['award'])
                subject = Subject.objects.get(subject_name=row['Subject'])
                answer = Answer.objects.get(answer_text=row['Answers'])


                Summary.objects.create(
                    school=school,
                    sydney_participant=row['participant'] == "Yes",
                    sydney_percentile=float(row['sydney_percentile']),
                    assessment_area=assessment_area,
                    award=award,
                    student_class=student_class,
                    correct_answer_percentage_per_class=float(row['correct_answer_percentage_per_class']),
                    correct_answer=int(row['Correct Answers']),
                    student=student,
                    participant=row['participant'] == "Yes",
                    student_score=int(row['student_score']),
                    subject=subject,
                    category_id=int(row['Question Number']),
                    year_level_name=row['Year Level'],
                    answer=answer,
                    correct_answer_id=int(row['correct_answer_id']),
                )

        # Optionally, load Awards if you have them
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Award.objects.get_or_create(name=row['award'])