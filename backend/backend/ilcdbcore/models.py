from django.db import models

# Create your models here.

class ojttrainee(models.Model):
    id = models.IntegerField(primary_key=True)
    province = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    ojt_duration = models.IntegerField()
    school_address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    contact_number = models.IntegerField()
    name_student = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    mode = models.CharField(max_length=255)
    recommendation_letter = models.FileField(upload_to='recommendation_letter/')
    application_form = models.FileField(upload_to='application_form/')
    cv_resume = models.FileField(upload_to='cv_resumes/')
    medical_certificate = models.FileField(upload_to='mde_cert/')
    workplan_form = models.FileField(upload_to='workplan_form/')
    interview_form_evaluation = models.BooleanField()
    acceptance_letter = models.BooleanField()
    wfh_arrangement = models.FileField(upload_to='wfh_arrangement/')
    nda = models.FileField(upload_to='nda/')
    work_assignment_schedule_form = models.FileField(upload_to='wa_schedform/')
    timesheet = models.FileField(upload_to='timesheet/')
    coc = models.FileField(upload_to='coc/')
    remarks = models.TextField()


    def __str__(self):
        return f"ojttrainee {self.id}"
