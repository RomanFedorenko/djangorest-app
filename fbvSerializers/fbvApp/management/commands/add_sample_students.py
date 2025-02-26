"""Management command to add sample students to the database."""

from django.core.management.base import BaseCommand
from fbvApp.models import Student


class Command(BaseCommand):
    """Django command to add sample students to the database."""

    help = 'Adds two sample students to the database'

    def handle(self, *args, **kwargs):
        """Execute the command to add sample students."""
        students = [
            Student(id=1, name='John Doe', score=95),
            Student(id=2, name='Jane Smith', score=88),
        ]

        try:
            Student.objects.bulk_create(students)
            self.stdout.write(
                self.style.SUCCESS('Successfully added two sample students')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error adding students: {str(e)}')
            ) 