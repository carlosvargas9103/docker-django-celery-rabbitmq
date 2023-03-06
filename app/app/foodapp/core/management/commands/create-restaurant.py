#https://docs.djangoproject.com/en/3.2/ref/django-admin/#syntax-coloring
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from core.models import Restaurant
from core.serializers import RestaurantSerializer
class Command(BaseCommand):
    
    help='''
    To create a new Restaurant (bz): 
    --name ["New Restaurant Name"] [100] (required)
    --type [Vegetarian, Vegan, Pescetarian, Halal, Kosher, Gluten-Free, OR Standard] as [Vegi, Vegn, Pesc, Hlal, Kosh, Gltf, OR Stnd] (optional)
    --email (required)
    '''
    
    def add_arguments(self, parser):
        p = parser        
        p.add_argument('-n','--name', type=str, nargs='?', required=False, default='New Restaurant Name', help='Restaurant name [100]')
        p.add_argument('-t','--type', type=str, nargs='?', required=False, default='Stnd', help='type of restaurant such as => [Vegi, Vegn, Pesc, Hlal, Kosh, Gltf, OR Stnd]')
        p.add_argument('-e','--email', type=str, nargs='?', required=True, default='', help='email of restaurant')
        
                
    """
    Checks if the Restaurant is valid and creates it. Otherwise, inform the user thru the terminal.
    """    
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Creating Restaurant..'))
        try:
            restaurant = Restaurant.objects.create(
                name=options['name'],
                res_type=options['type'],
                email=options['email']
            )
            print (restaurant)
            self.stdout.write(self.style.SUCCESS('The Restaurant was created successfully ;)'))
        except IntegrityError as e:
            self.stdout.write(self.style.NOTICE('Restaurant details are not valid'))
            #raise e        
        except Exception as e:
            #self.stdout.write(self.style.NOTICE('The Restaurant details are not valid'))
            raise e