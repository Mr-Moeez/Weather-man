from colorama import Fore

def get_max_min_temp_bar_chart(folder_path, year, month):
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

            print(month, year)
            for value in temp_data:
                for _ in range(value["max_temp"]):
                    print(Fore.RED + "+", end="")
                print(Fore.WHITE + str(value["max_temp"]) + "C")    
                for _ in range(value["min_temp"]):
                    print(Fore.BLUE +"-", end="")
                print(Fore.WHITE + str(value["min_temp"]) + "C")    
                print("\t")  
    except:
        print("Add Correct Arguments or press -h for more info")

















    # max_temperature_list = [int(value) for value in temp_data["max_temperature"] if value] 
    # min_temperature_list = [int(value) for value in temp_data["low_temperature"] if value] 
    
    # temp_data = {
    #         "max_temperature": max_temperature_list,
    #         "low_temperature": min_temperature_list
    #     } 
    
    # for maxMinTemp in temp_data:
        