from django.db import models
from datetime import datetime

# comment this next line of code if you migrate or have new database
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(
        self, email, password, first_name, last_name, mobile, province, **extra_fields
    ):

        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            province=province,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email, password, first_name, last_name, mobile, province, **extra_fields
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email, password, first_name, last_name, mobile, province, **extra_fields
        )

    def create_superuser(
        self, email, password, first_name, last_name, mobile, province, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email, password, first_name, last_name, mobile, province, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    province = models.CharField(max_length=250)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "mobile", "province"]

    class Meta:
        db_table = "User"


# until here ---------------------------------


class Intern_Table(models.Model):
    id = models.BigIntegerField(primary_key=True)
    province = models.CharField(max_length=100)
    school_name = models.CharField(max_length=200)
    ojt_duration = models.IntegerField()
    school_address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
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
        db_table = "Intern_Table"

    def save(self, *args, **kwargs):
        if not self.id:  # Only generate ID if it doesn't exist
            # Convert start_date to a date object if it's a string
            if isinstance(self.start_date, str):
                try:
                    self.start_date = datetime.strptime(
                        self.start_date, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    # Handle the case where start_date is not a valid date string
                    pass

            # Get current year from start_date
            current_year = self.start_date.year

            # Get the latest entry for the current year
            latest_entry = (
                Intern_Table.objects.filter(start_date__year=current_year)
                .order_by("-id")
                .first()
            )

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
    id = models.BigIntegerField(primary_key=True)
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

    def save(self, *args, **kwargs):
        # Check if the object is being saved for the first time
        if not self.pk:
            # Get the current maximum id value
            max_id = Engage_Partners_Table.objects.aggregate(models.Max("id"))[
                "id__max"
            ]
            # Set the id to the next available value
            self.id = max_id + 1 if max_id is not None else 10001
        super().save(*args, **kwargs)


class Training_Webinars_Table(models.Model):
    id = models.BigAutoField(primary_key=True)
    province = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    training_track = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    time = models.TimeField()
    total_num_hours = models.IntegerField() 
    nga_m = models.IntegerField()
    nga_f = models.IntegerField()
    suc_m = models.IntegerField()
    suc_f = models.IntegerField()
    lgu_m = models.IntegerField()
    lgu_f = models.IntegerField()
    others_m = models.IntegerField()
    others_f = models.IntegerField()
    total_m = models.IntegerField()
    total_f = models.IntegerField()
    total_participants = models.IntegerField()
    
    implementation_mode = models.CharField(max_length=255)
    
    resource_persons = models.TextField()

    course_officers = models.TextField()
    course_officers_email = models.TextField()
    remarks = models.TextField()
    
    participants_list = models.BinaryField()
    attendance_sheet = models.BinaryField()
    group_photo = models.BinaryField()
    certificates_issued = models.BinaryField()
    resource_persons_cv = models.BinaryField()

    class Meta:
        db_table = "Training_Webinars_Table"

    def save(self, *args, **kwargs):
        if not self.id:  # Only generate ID if it doesn't exist
            # Convert start_date to a date object if it's a string
            if isinstance(self.start_date, str):
                try:
                    self.start_date = datetime.strptime(
                        self.start_date, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    # Handle the case where start_date is not a valid date string
                    pass

            # Get current year from start_date
            current_year = self.start_date.year

            # Get the latest entry for the current year
            latest_entry = (
                Intern_Table.objects.filter(start_date__year=current_year)
                .order_by("-id")
                .first()
            )

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
                new_id = int(str(current_year) + "10001")

            self.id = new_id

        super().save(*args, **kwargs)



class Exam_Table(models.Model):
    id = models.AutoField(primary_key=True)
    province = models.CharField(max_length=100)
    name_of_examinee = models.CharField(max_length=255)
    venue_or_school = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    time = models.DateTimeField()
    status = models.CharField(max_length=20)
    remark_or_grade = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Exam_Table"
