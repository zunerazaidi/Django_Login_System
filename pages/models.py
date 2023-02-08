from django.db import models
class Member(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + ' ' + self.lname
