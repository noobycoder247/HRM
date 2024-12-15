from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SalaryUpdate(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary_updates')
    old_salary = models.DecimalField(max_digits=10, decimal_places=2)
    new_salary = models.DecimalField(max_digits=10, decimal_places=2)
    update_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.employee} on {self.update_timestamp}"
