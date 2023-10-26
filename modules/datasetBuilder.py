import pandas as pd
import requests

def datasetBuilder(data):
    if ('ResponseData' in data and 'error' in data['ResponseData'] and 'msg' in data['ResponseData']['error']):
        data = {
            'fromPlace': data['fromPlace'],
            'toPlace': data['toPlace'],
            'date': data['date'],
            'time': data['time'],
            'available': 'false',
            'trip': '', 
        }
        return (data)
    data['trip'] = data['ResponseData']['plan']['itineraries']
    data = {
        'fromPlace': data['fromPlace'],
        'toPlace': data['toPlace'],
        'date': data['date'],
        'time': data['time'],
        'available': 'true',
        'trip': data['trip'],
    }
    return (data)