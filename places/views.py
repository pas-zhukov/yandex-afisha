from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import Place


def index(request):
    places = get_places()
    context = {'geo_json': places}
    return render(request, 'index.html', context=context)


def place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    serialized_place = {
          "title": place.title,
          "imgs": [pic.image.url for pic in place.pictures.all().order_by('order_num')],
          "description_short": place.description_short,
          "description_long": place.description_long,
          "coordinates": {
            "lng": place.lat,
            "lat": place.long
          }
        }
    return JsonResponse(serialized_place, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})


def get_places(count: int = 100):
    places = Place.objects.all()
    serialized_places = {  # Сериализуем данные в формате GEO JSON
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
                    "detailsUrl": reverse('place-json', kwargs={'place_id': place.id})
                }
            } for place in places

        ]
    }
    return serialized_places
