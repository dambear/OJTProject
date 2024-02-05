from django.db import models

# Create your models here.
class OJT_Trainies(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=100)
    school_name = models.CharField(max_length=200)
    ojt_duration = models.IntegerField()
    school_address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    mode = models.CharField(max_length=20)
    recommendation_letter = models.BooleanField()
    application_form = models.BooleanField()
    cv_resume = models.BooleanField()
    medical_certificate = models.BooleanField()
    workplan_form = models.BooleanField()
    interview_form = models.BooleanField()
    acceptance_letter = models.BooleanField()
    wfh_arrangement = models.BooleanField()
    nda = models.BooleanField()
    work_assignment_form = models.BooleanField()
    war = models.BooleanField()
    timesheet = models.BooleanField()
    coc = models.BooleanField()
    remarks = models.TextField()

    def __str__(self):
        return self.student_name