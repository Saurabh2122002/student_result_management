# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Result(models.Model):
#     student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
#     passed = models.BooleanField(default=False)

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    # result = models.OneToOneField(Result, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.marks_obtained} "



