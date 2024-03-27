# myapp/views.py

from django.contrib.auth import authenticate, login, logout




from main.models import User

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            return redirect("/login")

    return render(request, "auth/_login.html", {})


def logout_page(request):
    logout(request)
    return redirect("/login")


def register_page(request):
    
    user_datas = User.objects.all()
    return render(request, "auth/_register/index.html", {"user_datas": user_datas})





@login_required(login_url="/login")
def view_data_register(request, user_id):
    
    user_data = get_object_or_404(User, id=user_id)
    return render(request, "auth/_register/view_data_register.html", {"user_data": user_data})



def add_data_register(request):
   
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile = request.POST['mobile']
        province = request.POST['province']


        # Create a new user
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            province=province
        )
        
        # Redirect to a success page or back to the form
        return redirect("register")

    return render(request, "auth/_register/add_data_register.html")


def update_data_register(request, user_id):
    
    user_data = get_object_or_404(User, id=user_id)
    
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile = request.POST['mobile']
        province = request.POST['province']

        
        # Update user data
        user_data.email = email
        user_data.set_password(password) # Use set_password to update the password
        user_data.first_name = first_name
        user_data.last_name = last_name
        user_data.mobile = mobile
        user_data.province = province
        user_data.save() # Don't forget to save the changes
     
        
        return redirect("register")
    
    return render(request, "auth/_register/update_data_register.html", {"user_data": user_data})


def delete_data_register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile = request.POST['mobile']
        province = request.POST['province']


        # Create a new user
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            province=province
        )
        
        return redirect("register")

    return render(request, "auth/_register/add_data_register.html", {})