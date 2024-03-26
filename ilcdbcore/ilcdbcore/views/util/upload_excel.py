import csv
from django.utils import timezone

from main.models import Intern_Table, Exam_Table, Engage_Partners_Table, Training_Webinars_Table


def upload_csv_data_to_intern_table(file_path):
    # Open the CSV file
    with open(file_path, 'r') as csvfile:
        # Create a CSV reader
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV
        for row in reader:
            # Create a new instance of the Intern_Table model
            intern = Intern_Table()
            # Set the fields with the data from the CSV
            intern.province = row.get('province')
            intern.school_name = row.get('school_name')
            intern.ojt_duration = int(row.get('ojt_duration'))
            intern.school_address = row.get('school_address')
            intern.contact_person = row.get('contact_person')
            intern.contact_number = row.get('contact_number')
            intern.student_name = row.get('student_name')
            intern.gender = row.get('gender')
            intern.start_date = timezone.datetime.strptime(row.get('start_date'), "%Y-%m-%d").date()
            intern.end_date = timezone.datetime.strptime(row.get('end_date'), "%Y-%m-%d").date()
            intern.mode = row.get('mode')
            intern.remarks = row.get('remarks')
            
            # Save the instance to the database
            intern.save()

def upload_csv_data_to_exam_table(file_path):
    # Open the CSV file
    with open(file_path, 'r') as csvfile:
        # Create a CSV reader
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV
        for row in reader:
            # Create a new instance of the Exam_Table model
            exam = Exam_Table()
            
            # Set the fields with the data from the CSV
            exam.province = row.get('province')
            exam.name_of_examinee = row.get('name_of_examinee')
            exam.venue_or_school = row.get('venue_or_school')
            exam.gender = row.get('gender')
            exam.time = timezone.datetime.strptime(row.get('time'), "%Y-%m-%d %H:%M:%S")
            exam.status = row.get('status')
            exam.remark_or_grade = row.get('remark_or_grade')
            
            # Save the instance to the database
            exam.save()



def upload_csv_data_to_training_webinars_table(file_path):
    # Open the CSV file
    with open(file_path, 'r') as csvfile:
        # Create a CSV reader
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV
        for row in reader:
            # Create a new instance of the Training_Webinars_Table model
            tmd = Training_Webinars_Table()
            
            # Set the fields with the data from the CSV
            tmd.province = row.get('province')
            tmd.course_name = row.get('course_name')
            tmd.training_track = row.get('training_track')
            tmd.start_date = timezone.datetime.strptime(row.get('start_date'), "%Y-%m-%d").date()
            tmd.end_date = timezone.datetime.strptime(row.get('end_date'), "%Y-%m-%d").date()
            tmd.time = timezone.datetime.strptime(row.get('time'), "%H:%M:%S").time()
            tmd.total_num_hours = int(row.get('total_num_hours'))
            tmd.nga_m = int(row.get('nga_m'))
            tmd.nga_f = int(row.get('nga_f'))
            tmd.suc_m = int(row.get('suc_m'))
            tmd.suc_f = int(row.get('suc_f'))
            tmd.lgu_m = int(row.get('lgu_m'))
            tmd.lgu_f = int(row.get('lgu_f'))
            tmd.others_m = int(row.get('others_m'))
            tmd.others_f = int(row.get('others_f'))
            tmd.total_m = int(row.get('total_m'))
            tmd.total_f = int(row.get('total_f'))
            tmd.total_participants = int(row.get('total_participants'))
            tmd.implementation_mode = row.get('implementation_mode')
            tmd.resource_persons = row.get('resource_persons')
            tmd.course_officers = row.get('course_officers')
            tmd.course_officers_email = row.get('course_officers_email')
            tmd.remarks = row.get('remarks')
            
            # Save the instance to the database
            tmd.save()
            
            
            
            
def upload_csv_data_to_engage_partners_table(file_path):
    # Open the CSV file
    with open(file_path, 'r') as csvfile:
        # Create a CSV reader
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV
        for row in reader:
            # Create a new instance of the Engage_Partners_Table model
            engage = Engage_Partners_Table()
            
            # Set the fields with the data from the CSV
            engage.province = row.get('province')
            engage.category = row.get('category')
            engage.name_of_partner_or_office = row.get('name_of_partner_or_office')
            engage.address = row.get('address')
            engage.contact_person = row.get('contact_person')
            engage.email = row.get('email')
            engage.contact_number = row.get('contact_number')
            engage.date_engaged = timezone.datetime.strptime(row.get('date_engaged'), "%Y-%m-%d").date()
            engage.engagement_mode = row.get('engagement_mode')
            engage.loi = row.get('loi')
            engage.remarks = row.get('remarks')
            
            # Save the instance to the database
            engage.save()
