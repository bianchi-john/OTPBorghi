import pandas as pd
from urllib.parse import quote


def datasetBuilder(data):
    if ('ResponseData' in data and 'error' in data['ResponseData'] and 'msg' in data['ResponseData']['error']):
        data = {
            'fromPlaceName': data['fromPlaceName'],
            'fromPalceCord': data['fromPalceCord'],
            'toPlaceName': data['toPlaceName'],
            'toPlaceCord': data['toPlaceCord'],
            'date': data['date'],
            'time': data['time'],
            'available': 'false',
            'duration': '',
            'startTime': '',
            'endTime': '',
            'walkTime': '',
            'walkDistance': '',
            'walkLimitExceeded': '',
            'generalizedCost': '',
            'elevationLost': '',
            'elevationGained': '',
            'transfers': '',
            'url_to_watch': "http://localhost:8080/?module=planner&fromPlace=" + quote(data['fromPalceCord']) + '&toPlace=' + quote(data['toPlaceCord']) + '&time=' + quote(data['time']) + '&date=' + quote(data['date'] + '&mode=TRANSIT%2CWALK&arriveBy=false&wheelchair=false&showIntermediateStops=true&additionalParameters=searchWindow&searchWindow=18000&locale=it&baseLayer=OSM%20Standard%20Tiles'),
        }
        return (data)
    try:
        data['trip'] = min(data['ResponseData']['plan']['itineraries'], key=lambda x: x['duration'])
    except:
        data = {
            'fromPlaceName': data['fromPlaceName'],
            'fromPalceCord': data['fromPalceCord'],
            'toPlaceName': data['toPlaceName'],
            'toPlaceCord': data['toPlaceCord'],
            'date': data['date'],
            'time': data['time'],
            'available': 'false',
            'duration': '',
            'startTime': '',
            'endTime': '',
            'walkTime': '',
            'walkDistance': '',
            'walkLimitExceeded': '',
            'generalizedCost': '',
            'elevationLost': '',
            'elevationGained': '',
            'transfers': '',
            'url_to_watch': "http://localhost:8080/?module=planner&fromPlace=" + quote(data['fromPalceCord']) + '&toPlace=' + quote(data['toPlaceCord']) + '&time=' + quote(data['time']) + '&date=' + quote(data['date'] + '&mode=TRANSIT%2CWALK&arriveBy=false&wheelchair=false&showIntermediateStops=true&additionalParameters=searchWindow&searchWindow=18000&locale=it&baseLayer=OSM%20Standard%20Tiles'),
        }
        return (data)
    data = {
        'fromPlaceName': data['fromPlaceName'],
        'fromPalceCord': data['fromPalceCord'],
        'toPlaceName': data['toPlaceName'],
        'toPlaceCord': data['toPlaceCord'],
        'date': data['date'],
        'time': data['time'],
        'available': 'true',
        'duration': data['trip']['duration'],
        'startTime': data['trip']['startTime'],
        'endTime': data['trip']['endTime'],
        'walkTime': data['trip']['walkTime'],
        'walkDistance': data['trip']['walkDistance'],
        'walkLimitExceeded': data['trip']['walkLimitExceeded'],
        'generalizedCost': data['trip']['generalizedCost'],
        'elevationLost': data['trip']['elevationLost'],
        'elevationGained': data['trip']['elevationGained'],
        'transfers': data['trip']['transfers'],
        'url_to_watch': "http://localhost:8080/?module=planner&fromPlace=" + quote(data['fromPalceCord']) + '&toPlace=' + quote(data['toPlaceCord']) + '&time=' + quote(data['time']) + '&date=' + quote(data['date'] + '&mode=TRANSIT%2CWALK&arriveBy=false&wheelchair=false&showIntermediateStops=true&additionalParameters=searchWindow&searchWindow=18000&locale=it&baseLayer=OSM%20Standard%20Tiles'),
        }
    return (data)