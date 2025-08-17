from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# --- Registration View ---
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# --- Login View (built-in, customized if needed) ---
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"


# --- Logout View (built-in) ---
class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
