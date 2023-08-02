from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json
from .models import Place, Picture


def index(request):
    template = loader.get_template('index.html')
    places = get_places()
    context = {
            'geo_json': places

                   }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)


def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_json = {
          "title": place.title,
          "imgs": [pic.image.url for pic in place.pictures.all().order_by('order_num')],
          "description_short": place.description_short,
          "description_long": place.description_long,
          "coordinates": {
            "lng": place.lat,
            "lat": place.long
          }
        }

    return JsonResponse(place_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def get_places(count: int = 100):
    places = Place.objects.all()

    geo_json = {
        "type": "FeatureCollection",
        "features": [

            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lat, place.long]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": f"places/{place.id}/"
                }
            } for place in places

        ]
    }

    return geo_json
