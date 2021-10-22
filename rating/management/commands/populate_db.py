from django.core.management.base import BaseCommand
import random
from rating.models import Rating

class Command(BaseCommand):
    help = 'padding some entries to Rating models'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        names = ['dom', 'tachka', 'shapka', 'noutbuk', 'stul', 'kreslo', 'etc']
        glac = ['a', 'o', 'u', 'i', 'y', 'e']
        from random import randint
        count = options.get('count', 1)

        # generate random name
        rate_name_list = []
        rate_name = ''
        for name in names:
            for n in name:
                rate_name_list.append(n)
            for letter in rate_name_list:
                s = random.choice(rate_name_list)
                if s not in glac:
                    rate_name += s
                else:
                    rate_name += s
        print(rate_name)
        for i in range(count):
            r = Rating(name=i, text="created from command line", rate=randint(1, 5))
            r.save()