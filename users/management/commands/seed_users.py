from django.core.management.base import BaseCommand
from faker import Faker

from users.models import User


fake = Faker()


class Command(BaseCommand):
    help = "Generate random users"

    def handle(self, *args, **kwargs):

        users = []

        for _ in range(100):

            users.append(
                User(
                    email=fake.unique.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    phone=fake.phone_number()[:20],
                    is_active=True,
                )
            )

        User.objects.bulk_create(users)

        self.stdout.write(
            self.style.SUCCESS(
                "100 users created"
            )
        )