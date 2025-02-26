from django.core.management.base import BaseCommand
from passengersApiApp.models import Passenger

class Command(BaseCommand):
    """Command to add two passengers to the database."""

    def handle(self, *args, **kwargs):
        """Handle the command execution."""
        passengers = [
            {'firstName': 'John', 'lastName': 'Doe', 'travelPoints': 100},
            {'firstName': 'Jane', 'lastName': 'Smith', 'travelPoints': 200},
        ]

        for passenger in passengers:
            Passenger.objects.create(**passenger)
            self.stdout.write(self.style.SUCCESS(f'Successfully added passenger: {passenger["firstName"]} {passenger["lastName"]}')) 