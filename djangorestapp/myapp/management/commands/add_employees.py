   # myapp/management/commands/add_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    """Command to add employees to the database."""

    help = 'Add employees to the database'

    def handle(self, *args, **kwargs):
        """Handle the command to add employees."""
        from myapp.models import Employee  # Import Employee model

        # Create or get employee with empId 1
        employee, created = Employee.objects.get_or_create(
            empId=1,
            defaults={
                'firstName': 'John',
                'lastName': 'Doe',
                'salary': 50000.000,
            },
        )

        # Create or get employee with empId 2
        employee2, created2 = Employee.objects.get_or_create(
            empId=2,
            defaults={
                'firstName': 'Jane',
                'lastName': 'Smith',
                'salary': 60000.000,
            },
        )

        # Output the result of the creation or existence of employee 1
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created employee with empId 1'))
        else:
            self.stdout.write(self.style.WARNING('Employee with empId 1 already exists'))

        # Output the result of the creation or existence of employee 2
        if created2:
            self.stdout.write(self.style.SUCCESS('Successfully created employee with empId 2'))
        else:
            self.stdout.write(self.style.WARNING('Employee with empId 2 already exists'))