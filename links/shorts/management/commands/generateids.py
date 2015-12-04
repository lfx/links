from django.core.management.base import BaseCommand, CommandError
from shorts.models import ShortList
from itertools import product
from string import ascii_lowercase, digits

class Command(BaseCommand):
    help = 'Generate short ids'

    def add_arguments(self, parser):
        parser.add_argument('size', nargs='+', type=int)

    def handle(self, *args, **options):
        size = options['size'][0]
        if size < 5:
            keywords = [''.join(i) for i in product(ascii_lowercase+digits, repeat = size)]
            for key in keywords:
                short = ShortList(short=key)
                short.save()

            self.stdout.write("Generated %s items" % len(keywords))
        else:
            self.stdout.write("Size is too big!!!!")
