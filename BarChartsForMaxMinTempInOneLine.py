from colorama import Fore

def get_max_min_temp_bar_chart_horizontally(folder_path, year, month):
    file_path = folder_path + "/" + folder_path + "_" + str(year) +"_"+ month + ".txt"
    try:
        with open(file_path, "r") as file:
            read_content = file.readlines()

            rows = [row.strip().split(',') for row in read_content[1:]]
            temp_data = []   
            for row in rows:
                if row[1] and row[3]:
                    max_temp = row[1]
                    min_temp = row[3]
                    temp_data.append({"max_temp": int(max_temp), "min_temp": int(min_temp)})
        print("Add correct Folder Path")
        print(month, year)
        for value in temp_data:
            for _ in range(value["min_temp"]):
                print(Fore.BLUE +"-", end="")
            for _ in range(value["max_temp"]):
                print(Fore.RED + "+", end="")
            print(Fore.WHITE + " " + str(value["min_temp"]) + "C - " + str(value["max_temp"]) + "C")    
            print("\t")    
    except:
         print("Add Correct Arguments or press -h for more info")