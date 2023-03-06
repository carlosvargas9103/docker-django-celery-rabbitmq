from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
 
class Command(BaseCommand):
    
    """
    Checks if the database when up has any users, else creates the initial admin user or show the admin credentials
    """
 
    def handle(self, *args, **options):        
        if User.objects.count() < 1:
            self.stdout.write(self.style.SUCCESS('Creating initial admin user...'))
            user = User.objects.create(username='django', is_staff=True, is_superuser=True)
            user.set_password('admin')
            user.save()
            self.stdout.write(self.style.SUCCESS('Successfully created initial admin superuser as:'))
            self.stdout.write(self.style.SUCCESS('username: django, password: admin'))
        else:
            self.stdout.write(self.style.SUCCESS('Initial admin creadentials are'))
            self.stdout.write(self.style.SUCCESS('username: django, password: admin'))