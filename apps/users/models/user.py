from django.db import models
import uuid # Gen. 36-bit Unique id for user entered in the DB Table.

class UserProfile(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable = False, unique = True)
    # It generates a UUID Version 4 — a random 128-bit unique identifier.

    name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, 
                              choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')] )
    educational_qualifications = models.CharField(max_length = 255)
    address = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"User {name} with Unique ID:{unique_id}"
