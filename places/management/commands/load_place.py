import os
from urllib.parse import urlparse, unquote
import json

import requests
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Picture
from django.core.files.base import ContentFile
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'Загружает локацию из json файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('json_source', nargs='*', type=str, help='JSON URL or path to JSON file.')

    def handle(self, *args, **options):
        for source in options['json_source']:
            if self.is_url(source):
                try:
                    place_response = requests.get(source)
                    place_response.raise_for_status()
                    place_params = place_response.json()
                except requests.HTTPError:
                    raise CommandError('HTTP Error! Check the JSON source link!')
            else:
                try:
                    with open(source, 'rb') as file:
                        place_params = json.load(file)
                except FileNotFoundError:
                    raise CommandError('File not found! Check the JSON source path!')

            defaults = {
                        'lat': place_params['coordinates']['lng'],
                        'long': place_params['coordinates']['lat'],
                        'description_short': place_params['description_short'],
                        'description_long': place_params['description_long']
            }
            place, _ = Place.objects.get_or_create(title=place_params['title'], defaults=defaults)
            self.upload_images(place, place_params['imgs'])
            self.stdout.write(self.style.SUCCESS(f'Successfully uploaded place "{place.title}".'))

    def upload_images(self, place: Place, img_urls: list[str]):
        for index, url in enumerate(img_urls):
            try:
                response = requests.get(url)
                response.raise_for_status()
                binary_image = response.content
                content = ContentFile(binary_image)
                filename = self.get_filename(url)
                pic = Picture.objects.create(title=filename, place=place)
                pic.image.save(filename, content, save=True)
            except requests.HTTPError:
                self.stdout.write(self.style.ERROR(f'URL #{index} is wrong, picture will be skipped.'))
                continue

    @staticmethod
    def get_filename(image_url: str) -> str:
        """Return the filename.

        :param image_url: The URL of the file.
        :return: Filename with extension
        """
        path_only = unquote(urlparse(image_url).path)
        filename = os.path.split(path_only)[1]
        return filename

    @staticmethod
    def is_url(source: str):
        """Check if source string is URL link."""
        validator = URLValidator()
        try:
            validator(source)
        except ValidationError:
            return False
        return True
