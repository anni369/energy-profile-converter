import json, argparse, copy
def converter():
    parser = argparse.ArgumentParser(
                prog='profile_converter.py',
                description='convert_energy-profile',
                epilog='Text at the bottom of help')
    parser.add_argument('input_filename') # user specifies: value # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument('output_filename')
    parser.add_argument('--interval', type = int, default=15, choices = [1,15, 30, 60, 1440] ) # user specifies: --name value # https://docs.python.org/3/library/argparse.html#choices
    parser.add_argument('--unit', default = "Wh", choices = ["kWh","Wh", "KJ", "J"])
    args = parser.parse_args()

    target_interval = args.interval
    target_unit = args.unit

    with open(args.input_filename, "r") as my_file, open(args.output_filename, "w") as output:
        data = my_file.read()
        data = json.loads(data)
        data_output = copy.copy(data)
        data_output["interval_in_minutes"] = target_interval
        data_output["unit"] = target_unit

        file_interval = data["interval_in_minutes"]
        file_unit = data["unit"]
        file_data = data["data"]

        #interval more frequent to less frequent data:
        converted_data = []
        if file_interval < target_interval:
            interval_step = target_interval // file_interval
            for i in range(0, len(file_data), interval_step):
                val_new = (sum(file_data[i: i+interval_step])) / interval_step
                converted_data.append(val_new)

        #interval less frequent to more frequent data:
        if file_interval > target_interval:
            interval_step = file_interval // target_interval
            for e in file_data:
                for i in range(0, interval_step):
                    converted_data.append(e)
            data_output["data"] = converted_data

        # data to unit:
        conv_dict = {}
        conv_dict["kWh"] = float (0.001)  # unit * target / file unit
        conv_dict["Wh"] = 1
        conv_dict["KJ"] = float (3.6)
        conv_dict["J"] = 3600
        if file_unit != target_unit:
            converted_data_units = []
            for e in data_output["data"]:
                e *= conv_dict[target_unit] / conv_dict[file_unit]
                converted_data_units.append(e)
            data_output["data"] = converted_data_units

        # writing the file:
        result = json.dump(data_output, output)
        return result

if __name__ == "__main__":
    converter()