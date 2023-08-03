import os
from urllib.parse import urlparse, unquote
import json

import requests
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Picture
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Загружает локацию из json файла в БД'

    def add_arguments(self, parser):
        parser.add_argument('json_url', nargs='*', type=str)

    def handle(self, *args, **options):
        for url in options['json_url']:
            try:
                place_json = self.get_json(url)
            except requests.HTTPError:
                raise CommandError('HTTP Error! Check the file!')
            except requests.exceptions.MissingSchema:
                place_json = json.loads(url)

            place = Place.objects.get_or_create(title=place_json['title'],
                                                lat=place_json['coordinates']['lng'],
                                                long=place_json['coordinates']['lat'])[0]

            place.description_short = place_json['description_short']
            place.description_long = place_json['description_long']
            place.save()
            self.upload_images(place, place_json['imgs'])
            self.stdout.write(self.style.SUCCESS('Successfully uploaded places.'))


    @staticmethod
    def get_json(url: str) -> dict:
        place = requests.get(url)
        place.raise_for_status()
        return place.json()

    def upload_images(self, place: Place, img_urls: list[str]):
        for index, url in enumerate(img_urls):
            try:
                content = self.download_image(url)
                filename = self.get_filename(url)
                pic = Picture.objects.create(title=filename, place=place)
                pic.image.save(filename, content, save=True)
            except requests.HTTPError:
                self.stdout.write(self.style.ERROR(f'URL #{index} is wrong, picture will be skipped.'))
                continue

    @staticmethod
    def download_image(url: str) -> ContentFile:
        response = requests.get(url)
        response.raise_for_status()
        binary_image = response.content
        return ContentFile(binary_image)

    @staticmethod
    def get_filename(image_url: str) -> str:
        """Return the filename.

        :param image_url: The URL of the file.
        :return: A tuple containing the filename and extension of the file.
        """
        path_only = unquote(urlparse(image_url).path)
        filename = os.path.split(path_only)[1]
        return filename
