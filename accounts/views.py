from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST

def signup_view(request): # Define signup view function that handles requests  
    if request.method == "POST": #Check if form has been submitted
        form = UserCreationForm(request.POST) # Create form instance with submitted data
        if form.is_valid(): # Check if form data is valid
            user = form.save() # Save new user to database
            login(request, user) # Login user immediately after signup
            return redirect("notes:list") # Redirect user to notes list page
    else: # If request is not POST (user just opened page)
        form = UserCreationForm() # Create an empty signup form
    return render(request, "accounts/signup.html", {"form": form}) # Render signup template with form


def login_view(request): # Define login view function that handles requests
    if request.method == "POST": # Check if form is submitted
        form = AuthenticationForm(data=request.POST) # Create login form with submitted data
        if form.is_valid(): # Validate login data
            user = form.get_user() # Get authenticated user object from form
            login(request, user) # Login user immediately
            return redirect("notes:list") # Take user to notes list page
    else: #If request is not post (Show user login page)
        form = AuthenticationForm() # Create empty login form
    return render(request, "accounts/login.html", {"form": form}) # Render login template with form

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request): # Define logout view function that handles requests
    logout(request) # Log the user out
    return redirect("login") # Take user to login in page