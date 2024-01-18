import pandas as pd
import requests
from libraries.datasetBuilder import datasetBuilder
import os

def apiCaller(place, places, dates, times):
    # Initialize a list of dictionaries to store data.
    data_list = []
    # API URL
    api_url = "http://localhost:8080/otp/routers/default/plan?"
    output_folder = 'datasetGenerator/output'  # Specific folder where you want to save the CSV files

    try:
        # First loop: from_place is the single place, and to_place is each place in the list
        for index, row in places.iterrows():
            from_place = place['LatLong']
            to_place = row['LatLong']

            # Check if the starting place is different from the destination place.
            if from_place != to_place:
                for date in dates:
                    for time in times:
                        params = {
                            'fromPlace': from_place,
                            'toPlace': to_place,
                            'date': date,
                            'time': time,
                            'mode': 'TRANSIT,WALK',
                            'arriveBy': 'false',
                            'wheelchair': 'false',
                            'showIntermediateStops': 'true',
                            'additionalParameters':'searchWindow',
                            'locale': 'it',
                            'searchWindow':'18000',
                        }
                        response = requests.get(api_url, params=params)
                        response.raise_for_status()  # Check if the request was successful
                        response_data = response.json()

                        # Create a dictionary containing the data and the answer
                        data_dict = {
                            'fromPlaceName': place['Comune'],
                            'fromPlaceCord': from_place,
                            'toPlaceName': row['Comune'],
                            'toPlaceCord': to_place,
                            'date': date,
                            'time': time,
                            'ResponseData': response_data
                        }
                        data_dict = datasetBuilder(data_dict)
                        data_list.append(data_dict)
    except requests.exceptions.RequestException as e:
        # Handle any errors in the API request.
        return f"Errore nella richiesta API: {str(e)}"
    # Creating the DataFrame from the list of dictionaries.
    data_df = pd.DataFrame(data_list)
    try:
        # Construct the CSV file path
        csv_file_path = os.path.join(output_folder, 'routes' + '.csv')
        if os.path.exists(csv_file_path):
            # If the CSV file already exists, append the data to it.
            existing_data = pd.read_csv(csv_file_path)
            updated_data = pd.concat([existing_data, data_df], ignore_index=True)
            updated_data.to_csv(csv_file_path, index=False)
        else:
            # If the CSV file doesn't exist, create a new one.
            data_df.to_csv(csv_file_path, index=False)
        return f'Dati recuperati per {str(place.Comune)} e salvati in {csv_file_path}'
    except Exception as e:
        # Managing CSV saving process
        return f"Error during csv saving: {str(e)}"
