import json, argparse
def converter():
    converted_data = []
    converted_data_units = []
    interval_step = 1
    try:
        """ parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')"""
        input_ = "example.json" #str(input("input_file: "))
        output_ = "output.json" #str(input("output_file: "))
        target_interval = 60 #int(input("Interval in minutes: "))
        target_units = "KJ" #str(input("Units: "))
        if target_interval != 1 or 15 or 30 or 60 or 1440:
            raise ValueError("Please, specify the valid interval in minutes: 1, 15, 30, 60 or 1440")
        if target_units.lower() != "kwh" or "wh" or "wj" or "j":
            raise ValueError("Please, specify the valid units: kWh, Wh, KJ or J")
    except:
        pass

    with open(input_, "r") as my_file, open(output_, "w") as output:
        data = my_file.read()
        data = json.loads(data)
        file_interval = data["interval_in_minutes"]
        file_units = data["unit"]
        file_data = data["data"]

        #interval more frequent to less frequent and data:
        if file_interval < target_interval:
            interval_step = target_interval // file_interval
            for i in range(0, len(file_data), interval_step):
                val_new = (sum(file_data[i : i+interval_step]))/ interval_step
                converted_data.append(val_new)
        #interval less frequent to more frequent and data:
        if file_interval > target_interval:
            interval_step = file_interval // target_interval
            file_interval = target_interval
            for e in file_data:
                for i in range (0, len(interval_step)):
                    converted_data.append(e)
        
        #data to unit:
        conv_dict = {}
        conv_dict["kwh"] = float (0.001)
        conv_dict["wh"] = 1
        conv_dict["kj"] = float (3.6)
        conv_dict["j"] =  3600
        conv_factor = conv_dict[file_units.lower()] // conv_dict[target_units.lower()]
        for e in converted_data:
            e *= conv_factor
            converted_data_units.append(e)

        file_data = converted_data
        # unit
        if file_units.lower() != target_units.lower():
            file_units = target_units

        #writing the file:
        output = json.dump(data, output)
        return output 
if __name__ == "__main__":
    converter()