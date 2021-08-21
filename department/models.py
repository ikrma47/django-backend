from django.db import models

# Create your models here.


class Departments(models.Model):

    id = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.departmentName


class Programs(models.Model):

    id = models.AutoField(primary_key=True)
    programName = models.CharField(max_length=100)
    department = models.ManyToManyField(
        to=Departments,
        related_name='programs',
        through='DepartmentProgram',
        through_fields=('program', 'department'))
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.programName


class DepartmentProgram(models.Model):

    id = models.AutoField(primary_key=True)
    program = models.ForeignKey(
        to=Programs, on_delete=models.CASCADE, related_name='+')
    department = models.ForeignKey(
        to=Departments, on_delete=models.CASCADE, related_name='+')
    courseCategory = models.CharField(max_length=3)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Department: {self.department}, Program: {self.program}, Course Category: {self.courseCategory}'
