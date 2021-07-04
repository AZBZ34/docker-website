from django.shortcuts import render
from django.http import HttpResponse
import socket
import requests
from .SQL.update_db import insert


def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    try:
        socket.inet_aton(ip)
        ip_valid = True
        print('Valid HTTP request from ' + str(ip))
    except socket.error:
        ip_valid = False

    geo_req = "https://geolocation-db.com/json/" + ip + "&position=true"
    response = requests.get(geo_req).json()

    response['user_ip'] = ip
    response['timestamp'] = ""
    insert(response)

    meetups = [
        {'title': 'A First meetup'},
        {'title': 'A second meetup'},
        {'title': 'A First meetup'},
        {'title': 'A second meetup'},
        {'title': 'A First meetup'},
        {'title': 'A second meetup'},
        {'title': 'A First meetup'},
        {'title': 'A second meetup'},
        {'title': 'A First meetup'},
        {'title': 'A second meetup'},
        {'title': 'A First meetup'},
        {'title': 'A second meetup'},
    ]

    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
        'ip': ip,
        'country_code': response['country_code'],
        'country_name': response['country_name'],
        'state': response['state'],
        'city': response['city'],
        'postal': response['postal'],
        'latitude': response['latitude'],
        'longitude': response['longitude'],
    })
