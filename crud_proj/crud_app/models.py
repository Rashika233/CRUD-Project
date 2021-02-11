from django.db import models
#DataFlair Models
class StudentModel(models.Model):
    id = models.IntegerField(primary_key = True)
    student_name = models.CharField(max_length=80)
    rollnumber = models.CharField(max_length=10)
    student_class = models.IntegerField()
    student_age = models.IntegerField()
 
    def __str__(self):
        return f"{self.student_name} : {self.rollnumber}"