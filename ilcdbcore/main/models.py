from django.db import models
from django.db.models import Max
from datetime import datetime

# Create your models here.


# table engage
class engage(models.Model):
    province = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    nameofoffice = models.CharField(max_length=255)
    contactnumber = models.CharField(max_length=11)

    class Meta:
        db_table = "engage"


# table ojt
class InternshipApplication(models.Model):
    ojt_duration = models.IntegerField()
    province = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)

    class Meta:
        db_table = "InternshipApplication"


class User_Table(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=50)
    province = models.CharField(max_length=100)

    class Meta:
        db_table = "User_Table"

    
class intern_table(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
    recommendation_letter = models.BooleanField(default=False)
    application_form = models.BooleanField(default=False)
    cv_resume = models.BooleanField(default=False)
    medical_certificate = models.BooleanField(default=False)
    workplan_form = models.BooleanField(default=False)
    interview_form = models.BooleanField(default=False)
    acceptance_letter = models.BooleanField(default=False)
    wfh_arrangement = models.BooleanField(default=False)
    nda = models.BooleanField(default=False)
    work_assignment_form = models.BooleanField(default=False)
    war = models.BooleanField(default=False)
    timesheet = models.BooleanField(default=False)
    coc = models.BooleanField(default=False)
    remarks = models.TextField()

    class Meta:
        db_table = "intern_table"

    def save(self, *args, **kwargs):
        if not self.id:  # Only generate ID if it doesn't exist
            # Convert start_date to a date object if it's a string
            if isinstance(self.start_date, str):
                try:
                    self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()
                except ValueError:
                    # Handle the case where start_date is not a valid date string
                    pass

            # Get current year from start_date
            current_year = self.start_date.year

            # Get the latest entry for the current year
            latest_entry = intern_table.objects.filter(
                start_date__year=current_year
            ).order_by('-id').first()
            
            if latest_entry:
                latest_id = latest_entry.id
                # Extract the last 4 digits from the latest_id
                last_four_digits = str(latest_id)[-4:]
                # Increment the last four digits by 1
                new_last_four_digits = int(last_four_digits) + 1
                # Construct the new_id
                new_id = int(str(current_year) + "{:04d}".format(new_last_four_digits))
            else:
                # If no entry exists for the current year, start at "1001"
                new_id = int(str(current_year) + "1001")

            self.id = new_id

        super().save(*args, **kwargs)
        
        
        
class Engage_Partners_Table(models.Model):
    id = models.BigAutoField(primary_key=True, default=10001)
    province = models.TextField()
    category = models.TextField()
    name_of_partner_or_office = models.TextField()
    address = models.TextField()
    contact_person = models.TextField()
    email = models.EmailField()
    contact_number = models.TextField()
    date_engaged = models.DateField()
    engagement_mode = models.TextField()
    loi = models.TextField()
    remarks = models.TextField()

    class Meta:
        db_table = "Engage_Partners_Table"




        
        