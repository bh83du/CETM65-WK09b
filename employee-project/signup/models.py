from django.db import models

# Create your models here.

class Users(models.Model):
    emp_no = models.CharField(max_length=6, unique=True, null=False)
    user_name = models.CharField(max_length=50, unique=False, null=False)
    dept = models.CharField(max_length=20, unique=False, null=True)
    email = models.EmailField(max_length=60, unique=True, null=False)
    password = models.CharField(max_length=30)

# Add Metadata - In this case, added to prevent
# Django Admin pluralising Users to Userss

    class Meta:
        verbose_name_plural = "Users"

# Define __str__ to be called when queried

def __str__(self):
    user_str = f"ID: {self.id}" \
               f"User ID: {self.emp_no}" \
               f"Name: {self.user_name}" \
               f"Department: {self.dept}" \
               f"Email: {self.email}" \
               f"Password: {self.password}" \

    return user_str    

