from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    """Класс для создания админа"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True,
        )
        user.set_password('123qwe456asd')
        user.save()
