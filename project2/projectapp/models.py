from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

from projectapp.validator import validate_file_size

# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_admin= models.BooleanField(default=False)

class Stud_reg(models.Model):
        user = models.OneToOneField(Login_view, on_delete=models.CASCADE, related_name='student', null=True)
        name = models.CharField(max_length=200)
        dob = models.DateField()
        phone_no = models.IntegerField()
        age = models.IntegerField(default=0)
        student_images = models.ImageField(upload_to="images",validators=[validate_file_size])

        def age(self):
            age = datetime.date.today() - self.dob
            return int((age).days / 365.25)


        def __str__(self):
            return self.name




class admin_reg(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE, primary_key=True,related_name='admin',null=False)
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
def __str__(self):
        return  self.name


class mark(models.Model):
    name = models.ForeignKey(Stud_reg,on_delete=models.CASCADE)
    phone = models.IntegerField()
    maths =models.IntegerField()
    physics =models.IntegerField()
    chemistry =models.IntegerField()

    def __str__(self):
        return self.name


