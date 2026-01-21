from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required # Require user to be loggin in to create a note
def note_list(request): # Define note_list function that handles requests
    notes = Note.objects.filter(user=request.user) # Get all notes that belong to user
    return render(request, "notes/note_list.html", {"notes": notes}) # Render note list template with notes

from .forms import NoteForm  # import the NoteForm class to create notes

@login_required # Require user to be logged in to create note
def note_create(request): # Define function that handles requests
    if request.method == "POST": # Check if form has been submitted
        form = NoteForm(request.POST) # Create form instance with submitted data
        if form.is_valid(): # Validate data
            note = form.save(commit=False) # Create not object but do not save yet
            note.user = request.user # Assign user as the owner of the note
            note.save() # Save the note to the database
            return redirect("notes:list") # Redirect to note list page after creation
    else: # If request not post (user views page)
        form = NoteForm() # Create empty note form
    return render(request, "notes/note_form.html", {"form": form}) # Render the note creation template with form

@ login_required # Require user to be logged in
def delete_note(request, note_id): # Define delete note function that handles request
    note = get_object_or_404(Note, id=note_id) # Get note by ID or show 404 if not found

    if request.method == "POST": # Check if delete form was submitted
        note.delete() # Delete note
        return redirect('notes:list') # Redirect to notes list page 
    return render(request, 'notes/delete_note.html', {'note': note}) # Render delete confirmation template

def home(request):
    return render(request, "notes/html.home")