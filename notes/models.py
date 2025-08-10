from django.db import models  # Import the toolbox that lets us describe data tables
from django.contrib.auth.models import User  # Bring in the ready-made user blueprint

class Note(models.Model):  # Create a new template called "Note"
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Every note belongs to one user; if the user is deleted, all their notes disappear too
    title = models.CharField(max_length=200)  # The note has a short headline, max 200 letters
    content = models.TextField()  # The note has a big open box for the main message
    created_at = models.DateTimeField(auto_now=True)  # Remember the exact date & time the note was last saved
    updated_at = models.DateTimeField(auto_now_add=True)  # Remember the exact date & time the note was first created

    def __str__(self):  # When the note is shown in a list, just display its title
        return self.title
