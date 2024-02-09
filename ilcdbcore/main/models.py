from django.db import models

# Create your models here.
        
# table engage
class engage(models.Model):
    province = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    nameofoffice = models.CharField(max_length=255)
    contactnumber = models.CharField(max_length=11)

    class Meta:
        db_table = 'engage'

# table ojt 
class InternshipApplication(models.Model):
    ojt_duration = models.IntegerField()
    province = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)

    class Meta:
        db_table = 'InternshipApplication'