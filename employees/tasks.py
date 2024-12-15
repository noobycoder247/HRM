from celery import shared_task
from datetime import date, timedelta
from .models import Employee, SalaryUpdate

@shared_task
def add_bonus_to_salaries():
    employees = Employee.objects.filter(date_of_joining__lt=date.today() - timedelta(days=365))
    for employee in employees:
        old_salary = employee.salary
        new_salary = old_salary * 1.05  # 5% bonus
        employee.salary = new_salary
        employee.save()

        # Log the update
        SalaryUpdate.objects.create(
            employee=employee,
            old_salary=old_salary,
            new_salary=new_salary
        )
