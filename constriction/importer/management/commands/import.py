import json
import logging

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.db import transaction
from investments.models import Investment

logger = logging.getLogger("constriction.console")


class Command(BaseCommand):
    help = 'Imports investments data from json file'

    def add_arguments(self, parser):
        parser.add_argument('input', type=str)
        parser.add_argument("--limit", "-l", type=int)

    def handle(self, *args, **options):
        items = []
        with open(options['input']) as input_file:
            items = json.load(input_file)
        
        if 'limit' in options:
            items = items[:options['limit']]


        with transaction.atomic():
            for item in items:
                investment = Investment()
                investment.title = item.get("title", "No title")
                investment.descritpion = item.get("description", "No description")
                investment.url = item.get("url", None)
                investment.url = item.get("price", None)
                investment.save()
