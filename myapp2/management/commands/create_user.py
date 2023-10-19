from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        user = User(name='Joe', email='joe@mail.com', password='secs', age=25)

        user.save()
        self.stdout.write(f'{user}')
