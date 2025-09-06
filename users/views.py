from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.http import HttpResponse

def home(request):
    return redirect("login") 

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})



def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def patient_dashboard(request):
    return render(request, "patient_dashboard.html", {"user": request.user})

@login_required
def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html", {"user": request.user})


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             # Redirect based on user type
#             if user.user_type == "patient":
#                 print("Redirecting to Patient Dashboard")
#                 return redirect("patient_dashboard")
#             elif user.user_type == "doctor":
#                 print("Redirecting to Doctor Dashboard")
#                 return redirect("doctor_dashboard")
#             else:
#                 # No generic dashboard → redirect to login or home instead
#                 return redirect("login")  
#         return render(request, "login.html", {"error": "Invalid credentials"})
#     return render(request, "login.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # 🔹 Check for ?next= in URL or hidden input
            next_url = request.GET.get("next") or request.POST.get("next")
            if next_url:
                return redirect(next_url)

            # 🔹 Fallback: redirect based on user type
            if user.user_type == "patient":
                print("Redirecting to Patient Dashboard")
                return redirect("patient_dashboard")
            elif user.user_type == "doctor":
                print("Redirecting to Doctor Dashboard")
                return redirect("doctor_dashboard")
            else:
                return redirect("login")  # fallback

        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")
