import glob
from datetime import datetime

def get_highest_temperature(folder_path, year):

    file_pattern= folder_path + '_' + str(year) +'_*.txt'

    all_rows = []

    file_list = glob.glob(folder_path + "/" + file_pattern)
    try:
        for file_path in file_list:
            with open(file_path, 'r') as file:
                data = file.readlines()
                rows = [row.strip().split(',') for row in data[1:]]
                all_rows.extend(rows)
        data = {
            "date": [],
            "max_temperature": [],
            "low_temperature": [],
            "max_humidity": [],
        }
        for row in all_rows:
            data["date"].append(row[0])
            data["max_temperature"].append(row[1])
            data["low_temperature"].append(row[3])
            data["max_humidity"].append(row[7])

        filtereMaxTemp = [int(value) for value in data["max_temperature"] if value]
        maxTemp = max(filtereMaxTemp)
        max_temp_unformatted_date = data["date"][data["max_temperature"].index(str(maxTemp))]
        max_temp_unformatted_date = datetime.strptime(max_temp_unformatted_date, '%Y-%m-%d')
        max_temp_formatted_date = max_temp_unformatted_date.strftime('%B %d')

        filtereMinTemp = [int(value) for value in data["low_temperature"] if value and value != 0]
        minTemp = min(filtereMinTemp)
        min_temp_unformatted_date = data["date"][data["low_temperature"].index(str(minTemp))]
        min_temp_unformatted_date = datetime.strptime(min_temp_unformatted_date, '%Y-%m-%d')
        min_temp_formatted_date = min_temp_unformatted_date.strftime('%B %d')

        filtereMaxHumidity = [int(value) for value in data["max_humidity"] if value and value != 0]
        maxHumidity = max(filtereMaxHumidity)
        humidity_unformatted_Date = data["date"][data["max_humidity"].index(str(maxHumidity))]
        humidity_unformatted_Date = datetime.strptime(humidity_unformatted_Date, '%Y-%m-%d')
        humidity_formatted_date = humidity_unformatted_Date.strftime('%B %d')


        print("Highest:", maxTemp,"C on", max_temp_formatted_date)    
        print("Lowest:", minTemp,"C on", min_temp_formatted_date)    
        print("Humid:", maxHumidity,"% on", humidity_formatted_date)
    except:
        print("Add Correct Arguments or press -h for more info")