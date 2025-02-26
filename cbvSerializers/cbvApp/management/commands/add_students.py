from django.core.management.base import BaseCommand
from cbvApp.models import Student

class Command(BaseCommand):
    """Command to add two students to the database."""

    def handle(self, *args, **kwargs):
        """Handle the command execution."""
        students = [
            {'id': 1, 'name': 'Alice', 'score': 85},
            {'id': 2, 'name': 'Bob', 'score': 90},
        ]

        for student in students:
            Student.objects.create(**student)
            self.stdout.write(self.style.SUCCESS(f'Successfully added student: {student["name"]} with score: {student["score"]}')) 