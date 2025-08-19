from django.db import models

# Create your models here.


class Students(models.Model):
  user_id = models.IntegerField()
  password = models.CharField( max_length=50)
  email = models.EmailField(null=True)
  name = models.CharField( max_length=100)
  
  def __str__(self):
    return f'{self.name}'
  

  
class Instructor(models.Model):
  name = models.CharField(max_length=100)
  

  def __str__(self):
     return f'{self.name}'



class Subject(models.Model):
    subject_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(
        Instructor, on_delete=models.SET_NULL, null=True, related_name='subjects'
    )
    credit = models.DecimalField(max_digits=4, decimal_places=2)
    students = models.ManyToManyField(
        Students,
        through='Enrollment',
        through_fields=('subject', 'student'),
        related_name='subjects'
    )

    def __str__(self):
       return f'{self.name}'

class Enrollment(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='enrollments')
    mark = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('student', 'subject')

  
