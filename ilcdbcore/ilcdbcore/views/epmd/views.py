from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from main.models import Intern_Table, Engage_Partners_Table, Exam_Table, Training_Webinars_Table, Limit_Table

@login_required(login_url="/login")
def index(request):
    
    user = request.user
    
    
    #cavite
    if user.province.lower() == "cavite":
        
        if not Limit_Table.objects.exists():
            Limit_Table.objects.create()
    
        cavite_count_ojt = Intern_Table.objects.filter(province__iexact="Cavite").count()
        cavite_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Cavite").count()
        cavite_count_exam = Exam_Table.objects.filter(province__iexact="Cavite").count()
        cavite_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Cavite").count()

        

        exam_cavite_limit = Limit_Table.objects.get(id=1).exam_cavite_limit
        ojt_cavite_limit = Limit_Table.objects.get(id=1).ojt_cavite_limit
        engage_cavite_limit = Limit_Table.objects.get(id=1).engage_cavite_limit
        tmd_cavite_limit = Limit_Table.objects.get(id=1).tmd_cavite_limit

        
        context = {
            'count_ojt': cavite_count_ojt,
            'count_engage': cavite_count_engage,
            'count_exam': cavite_count_exam,
            'count_tmd': cavite_count_tmd,
            
            'exam_limit' : exam_cavite_limit,
            'ojt_limit' : ojt_cavite_limit,
            'engage_limit' : engage_cavite_limit,
            'tmd_limit' : tmd_cavite_limit,

            
        }
        
        return render(request, "1_dash/dash_province.html", context)
    
    
    #Laguna
    if user.province.lower() == "laguna":
        
        if not Limit_Table.objects.exists():
            Limit_Table.objects.create()
    
        laguna_count_ojt = Intern_Table.objects.filter(province__iexact="Laguna").count()
        laguna_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Laguna").count()
        laguna_count_exam = Exam_Table.objects.filter(province__iexact="Laguna").count()
        laguna_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Laguna").count()

        

        exam_laguna_limit = Limit_Table.objects.get(id=1).exam_laguna_limit
        ojt_laguna_limit = Limit_Table.objects.get(id=1).ojt_laguna_limit
        engage_laguna_limit = Limit_Table.objects.get(id=1).engage_laguna_limit
        tmd_laguna_limit = Limit_Table.objects.get(id=1).tmd_laguna_limit

        
        context = {
            'count_ojt': laguna_count_ojt,
            'count_engage': laguna_count_engage,
            'count_exam': laguna_count_exam,
            'count_tmd': laguna_count_tmd,
            
            'exam_limit' : exam_laguna_limit,
            'ojt_limit' : ojt_laguna_limit,
            'engage_limit' : engage_laguna_limit,
            'tmd_limit' : tmd_laguna_limit,

            
        }
        
        return render(request, "1_dash/dash_province.html", context)
    
    
    #BATANGASSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    if user.province.lower() == "batangas":
        
        if not Limit_Table.objects.exists():
            Limit_Table.objects.create()
    
        batangas_count_ojt = Intern_Table.objects.filter(province__iexact="Batangas").count()
        batangas_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Batangas").count()
        batangas_count_exam = Exam_Table.objects.filter(province__iexact="Batangas").count()
        batangas_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Batangas").count()

        

        exam_batangas_limit = Limit_Table.objects.get(id=1).exam_batangas_limit
        ojt_batangas_limit = Limit_Table.objects.get(id=1).ojt_batangas_limit
        engage_batangas_limit = Limit_Table.objects.get(id=1).engage_batangas_limit
        tmd_batangas_limit = Limit_Table.objects.get(id=1).tmd_batangas_limit

        
        context = {
            'count_ojt': batangas_count_ojt,
            'count_engage': batangas_count_engage,
            'count_exam': batangas_count_exam,
            'count_tmd': batangas_count_tmd,
            
            'exam_limit' : exam_batangas_limit,
            'ojt_limit' : ojt_batangas_limit,
            'engage_limit' : engage_batangas_limit,
            'tmd_limit' : tmd_batangas_limit,

            
        }
        
        return render(request, "1_dash/dash_province.html", context)
    
    #RIZALLLLLLLLLLLLLLLLLLLLLLLLLLLL
    if user.province.lower() == "rizal":
        
        if not Limit_Table.objects.exists():
            Limit_Table.objects.create()
    
        rizal_count_ojt = Intern_Table.objects.filter(province__iexact="Rizal").count()
        rizal_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Rizal").count()
        rizal_count_exam = Exam_Table.objects.filter(province__iexact="Rizal").count()
        rizal_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Rizal").count()

        

        exam_rizal_limit = Limit_Table.objects.get(id=1).exam_rizal_limit
        ojt_rizal_limit = Limit_Table.objects.get(id=1).ojt_rizal_limit
        engage_rizal_limit = Limit_Table.objects.get(id=1).engage_rizal_limit
        tmd_rizal_limit = Limit_Table.objects.get(id=1).tmd_rizal_limit

        
        context = {
            'count_ojt': rizal_count_ojt,
            'count_engage': rizal_count_engage,
            'count_exam': rizal_count_exam,
            'count_tmd': rizal_count_tmd,
            
            'exam_limit' : exam_rizal_limit,
            'ojt_limit' : ojt_rizal_limit,
            'engage_limit' : engage_rizal_limit,
            'tmd_limit' : tmd_rizal_limit,

            
        }
        
        return render(request, "1_dash/dash_province.html", context)
    
    #QUEZONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
    if user.province.lower() == "quezon":
        
        if not Limit_Table.objects.exists():
            Limit_Table.objects.create()
    
        quezon_count_ojt = Intern_Table.objects.filter(province__iexact="Quezon").count()
        quezon_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Quezon").count()
        quezon_count_exam = Exam_Table.objects.filter(province__iexact="Quezon").count()
        quezon_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Quezon").count()

        

        exam_quezon_limit = Limit_Table.objects.get(id=1).exam_quezon_limit
        ojt_quezon_limit = Limit_Table.objects.get(id=1).ojt_quezon_limit
        engage_quezon_limit = Limit_Table.objects.get(id=1).engage_quezon_limit
        tmd_quezon_limit = Limit_Table.objects.get(id=1).tmd_quezon_limit

        
        context = {
            'count_ojt': quezon_count_ojt,
            'count_engage': quezon_count_engage,
            'count_exam': quezon_count_exam,
            'count_tmd': quezon_count_tmd,
            
            'exam_limit' : exam_quezon_limit,
            'ojt_limit' : ojt_quezon_limit,
            'engage_limit' : engage_quezon_limit,
            'tmd_limit' : tmd_quezon_limit,

            
        }
        
        return render(request, "1_dash/dash_province.html", context)
    
    #admin or all
    else:
        if not Limit_Table.objects.exists():
            Limit_Table.objects.create()
        
        cavite_count_ojt = Intern_Table.objects.filter(province__iexact="Cavite").count()
        laguna_count_ojt = Intern_Table.objects.filter(province__iexact="Laguna").count()
        batangas_count_ojt = Intern_Table.objects.filter(province__iexact="Batangas").count()
        rizal_count_ojt = Intern_Table.objects.filter(province__iexact="Rizal").count()
        quezon_count_ojt = Intern_Table.objects.filter(province__iexact="Quezon").count()
        
        cavite_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Cavite").count()
        laguna_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Laguna").count()
        batangas_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Batangas").count()
        rizal_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Rizal").count()
        quezon_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Quezon").count()
        
        cavite_count_exam = Exam_Table.objects.filter(province__iexact="Cavite").count()
        laguna_count_exam = Exam_Table.objects.filter(province__iexact="Laguna").count()
        batangas_count_exam = Exam_Table.objects.filter(province__iexact="Batangas").count()
        rizal_count_exam = Exam_Table.objects.filter(province__iexact="Rizal").count()
        quezon_count_exam = Exam_Table.objects.filter(province__iexact="Quezon").count()
        
        cavite_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Cavite").count()
        laguna_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Laguna").count()
        batangas_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Batangas").count()
        rizal_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Rizal").count()
        quezon_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Quezon").count()
        
        
        exam_cavite_limit = Limit_Table.objects.get(id=1).exam_cavite_limit
        exam_laguna_limit = Limit_Table.objects.get(id=1).exam_laguna_limit
        exam_batangas_limit = Limit_Table.objects.get(id=1).exam_batangas_limit
        exam_rizal_limit = Limit_Table.objects.get(id=1).exam_rizal_limit
        exam_quezon_limit = Limit_Table.objects.get(id=1).exam_quezon_limit

        
        ojt_cavite_limit = Limit_Table.objects.get(id=1).ojt_cavite_limit
        ojt_laguna_limit = Limit_Table.objects.get(id=1).ojt_laguna_limit
        ojt_batangas_limit = Limit_Table.objects.get(id=1).ojt_batangas_limit
        ojt_rizal_limit = Limit_Table.objects.get(id=1).ojt_rizal_limit
        ojt_quezon_limit = Limit_Table.objects.get(id=1).ojt_quezon_limit
        
        
        engage_cavite_limit = Limit_Table.objects.get(id=1).engage_cavite_limit
        engage_laguna_limit = Limit_Table.objects.get(id=1).engage_laguna_limit
        engage_batangas_limit = Limit_Table.objects.get(id=1).engage_batangas_limit
        engage_rizal_limit = Limit_Table.objects.get(id=1).engage_rizal_limit
        engage_quezon_limit = Limit_Table.objects.get(id=1).engage_quezon_limit
        
        
        tmd_cavite_limit = Limit_Table.objects.get(id=1).tmd_cavite_limit
        tmd_laguna_limit = Limit_Table.objects.get(id=1).tmd_laguna_limit
        tmd_batangas_limit = Limit_Table.objects.get(id=1).tmd_batangas_limit
        tmd_rizal_limit = Limit_Table.objects.get(id=1).tmd_rizal_limit
        tmd_quezon_limit = Limit_Table.objects.get(id=1).tmd_quezon_limit
        
        
        context = {
            'cavite_count_ojt': cavite_count_ojt,
            'laguna_count_ojt': laguna_count_ojt,
            'batangas_count_ojt': batangas_count_ojt,
            'rizal_count_ojt': rizal_count_ojt,
            'quezon_count_ojt': quezon_count_ojt,
            
            'cavite_count_engage': cavite_count_engage,
            'laguna_count_engage': laguna_count_engage,
            'batangas_count_engage': batangas_count_engage,
            'rizal_count_engage': rizal_count_engage,
            'quezon_count_engage': quezon_count_engage,
            
            'cavite_count_exam': cavite_count_exam,
            'laguna_count_exam': laguna_count_exam,
            'batangas_count_exam': batangas_count_exam,
            'rizal_count_exam': rizal_count_exam,
            'quezon_count_exam': quezon_count_exam,
            
            'cavite_count_tmd': cavite_count_tmd,
            'laguna_count_tmd': laguna_count_tmd,
            'batangas_count_tmd': batangas_count_tmd,
            'rizal_count_tmd': rizal_count_tmd,
            'quezon_count_tmd': quezon_count_tmd,
            
            
            'exam_cavite_limit' : exam_cavite_limit,
            'exam_laguna_limit' : exam_laguna_limit,
            'exam_batangas_limit' : exam_batangas_limit,
            'exam_rizal_limit' : exam_rizal_limit,
            'exam_quezon_limit' : exam_quezon_limit,

            
            'ojt_cavite_limit' : ojt_cavite_limit,
            'ojt_laguna_limit' : ojt_laguna_limit,
            'ojt_batangas_limit' : ojt_batangas_limit,
            'ojt_rizal_limit' : ojt_rizal_limit,
            'ojt_quezon_limit' : ojt_quezon_limit,
            
            
            'engage_cavite_limit' : engage_cavite_limit,
            'engage_laguna_limit' : engage_laguna_limit,
            'engage_batangas_limit' : engage_batangas_limit,
            'engage_rizal_limit' : engage_rizal_limit,
            'engage_quezon_limit' : engage_quezon_limit,
        
            
            'tmd_cavite_limit' : tmd_cavite_limit,
            'tmd_laguna_limit' : tmd_laguna_limit,
            'tmd_batangas_limit' : tmd_batangas_limit,
            'tmd_rizal_limit' : tmd_rizal_limit,
            'tmd_quezon_limit' : tmd_quezon_limit,
            
            
            
        }
        
        
        return render(request, "1_dash/index.html", context)





@login_required(login_url="/login")
def dash_province(request):
    if not Limit_Table.objects.exists():
        Limit_Table.objects.create()
    
    cavite_count_ojt = Intern_Table.objects.filter(province__iexact="Cavite").count()
    cavite_count_engage = Engage_Partners_Table.objects.filter(province__iexact="Cavite").count()
    cavite_count_exam = Exam_Table.objects.filter(province__iexact="Cavite").count()
    cavite_count_tmd = Training_Webinars_Table.objects.filter(province__iexact="Cavite").count()

    

    exam_cavite_limit = Limit_Table.objects.get(id=1).exam_cavite_limit
    ojt_cavite_limit = Limit_Table.objects.get(id=1).ojt_cavite_limit
    engage_cavite_limit = Limit_Table.objects.get(id=1).engage_cavite_limit
    tmd_cavite_limit = Limit_Table.objects.get(id=1).tmd_cavite_limit

    
    context = {
        'cavite_count_ojt': cavite_count_ojt,
        'cavite_count_engage': cavite_count_engage,
        'cavite_count_exam': cavite_count_exam,
        'cavite_count_tmd': cavite_count_tmd,
        
        'exam_cavite_limit' : exam_cavite_limit,
        'ojt_cavite_limit' : ojt_cavite_limit,
        'engage_cavite_limit' : engage_cavite_limit,
        'tmd_cavite_limit' : tmd_cavite_limit,

        
    }
    
    return render(request, "1_dash/dash_province.html", context)