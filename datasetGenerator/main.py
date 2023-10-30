import pandas as pd
from libraries.apiCaller import apiCaller
import os

# Delete the contents of the directory "output"
directory_path = "datasetGenerator/output"
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"Error deleting files in the directory: {str(e)}")


dates = ['10-01-2023','10-04-2023','05-06-2023','05-09-2023']
times = ['1:00pm', '2:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm', '7:00pm', '8:00pm', '9:00pm', '10:00pm', '11:00pm', '12:00pm', '1:00am', '2:00am', '3:00am', '4:00am', '5:00am', '6:00am', '7:00am', '8:00am', '9:00am', '10:00am', '11:00am', '12:00am']

places = pd.read_csv('paths.csv')

for i in range(len(places)):
    place = places.iloc[i]
    print('Getting data for ' + place.Comune)
    try:
        data = apiCaller(place, places, dates, times)
        print(data) 
    except Exception as e:
        print(f'Error during data recovery for {place.Comune}: {str(e)}')
