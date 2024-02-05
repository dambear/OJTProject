from ninja import ModelSchema, Schema
from api.models import OJT_Trainies



class OJT_TrainiesSchema(ModelSchema):
    class Meta:
        model = OJT_Trainies
        fields = [
            'id', 'province', 'school_name', 'ojt_duration', 'school_address',
            'contact_person', 'contact_number', 'student_name', 'sex', 'start_date',
            'end_date', 'mode', 'recommendation_letter', 'application_form',
            'cv_resume', 'medical_certificate', 'workplan_form', 'interview_form',
            'acceptance_letter', 'wfh_arrangement', 'nda', 'work_assignment_form',
            'war', 'timesheet', 'coc', 'remarks'
        ]
        
        
# create a new ojt
class OJT_TrainiesCreateSchema(Schema):
    province: str
    school_name: str
    ojt_duration: int
    school_address: str
    contact_person: str
    contact_number: str
    student_name: str
    sex: str
    start_date: str  # You may want to adjust this based on your date format
    end_date: str    # You may want to adjust this based on your date format
    mode: str
    recommendation_letter: bool
    application_form: bool
    cv_resume: bool
    medical_certificate: bool
    workplan_form: bool
    interview_form: bool
    acceptance_letter: bool
    wfh_arrangement: bool
    nda: bool
    work_assignment_form: bool
    war: bool
    timesheet: bool
    coc: bool
    remarks: str