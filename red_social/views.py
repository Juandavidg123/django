from django.http import HttpResponse
from datetime import datetime
import json


def hello_world(request):

    return HttpResponse('Hola {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message = 'No puedes entrar {}'.format(name)
    else:
        message = 'Hola, {}'.format(name)
    return HttpResponse(message)
