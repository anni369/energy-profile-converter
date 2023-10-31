import json, argparse
import copy
def converter():
    converted_data = []
    converted_data_units = []
    interval_step = 1

    parser = argparse.ArgumentParser(
                prog='profile_converter.py',
                description='convert_energy-profile',
                epilog='Text at the bottom of help')
    parser.add_argument('input_filename') # user specifies: value # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument('output_filename')
    parser.add_argument('--interval', type = int, default=60, choices = [1,15, 30, 60, 1440] ) # user specifies: --name value # https://docs.python.org/3/library/argparse.html#choices
    parser.add_argument('--unit', default = "KJ", choices = ["kWh","Wh", "KJ", "J"])
    args = parser.parse_args()

    input_ = args.input_filename
    output_ = args.output_filename
    target_interval = args.interval
    target_unit = args.unit

    with open(input_, "r") as my_file, open(args.output_filename, "w") as output:
        data = my_file.read()
        data = json.loads(data)
        data_output = copy.copy(data)
        data_output["interval_in_minutes"] = target_interval
        data_output["unit"] = target_unit

        file_interval = data["interval_in_minutes"]
        file_units = data["unit"]
        file_data = data["data"]

        #interval more frequent to less frequent and data:
        if file_interval < target_interval:
            interval_step = target_interval // file_interval
            for i in range(0, len(file_data), interval_step):
                val_new = (sum(file_data[i: i+interval_step])) / interval_step
                converted_data.append(val_new)

        #interval less frequent to more frequent and data:
        if file_interval > target_interval:
            interval_step = file_interval // target_interval
            file_interval = target_interval
            for e in file_data:
                for i in range (0, len(interval_step)):
                    converted_data.append(e)

        # data to unit:
        conv_dict = {}
        conv_dict["kWh"] = float (0.001)  # value [Wh] * dict[unit] = value in unit, value [unit] / dict[unit] = value in wH
        conv_dict["Wh"] = 1
        conv_dict["KJ"] = float (3.6)
        conv_dict["J"] = 3600
        conv_factor = conv_dict[file_units] / conv_dict[target_unit]
        for e in converted_data:
            e *= conv_factor
            converted_data_units.append(e)

        file_data = converted_data
        # unit
        if file_units != target_unit:
            file_units = target_unit

        # writing the file:
        print(data_output)
        result = json.dump(data_output, output)
        return result

if __name__ == "__main__":
    converter()