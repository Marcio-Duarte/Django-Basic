from django.db import models

# Create your models here.


class User(models.Model):
    idNumber = models.IntegerField(unique=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + self.lastName


class AccessRecord(models.Model):
    idNumber = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()
    
    def __str__(self):
        return str(self.date)
