from django.http import HttpResponse
from django.template import loader
import json

def index(request):
    template = loader.get_template('index.html')
    with open('static/places/geo_json.json', 'rb') as file:
        places = json.load(file)
        context = {
            'geo_json': places

                   }
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)