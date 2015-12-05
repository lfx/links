from django.core.management.base import BaseCommand, CommandError
from shorts.models import ShortList
from itertools import product
from string import ascii_lowercase, digits

class Command(BaseCommand):
    help = 'Generate short ids'

    def add_arguments(self, parser):
        parser.add_argument('size', nargs='+', type=int)

    def symbols(self, size):
        sym = (letter for letter in product(ascii_lowercase+digits, repeat=size))
        for symbol in sym:
            yield symbol

    def handle(self, *args, **options):
        size = options['size'][0]
        enums = enumerate(self.symbols(size))
        for i, word in enums:
            short = ShortList(short=''.join(word))
            short.save()
            print(i, ''.join(word))
