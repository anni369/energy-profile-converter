import json, argparse, copy
from argparse import Namespace
def setup_argparse() -> Namespace:
    """
    take user input from the command line
    :return: the parsed arguments
    """
    parser = argparse.ArgumentParser(
        prog='profile_converter.py',
        description='This program is able to read a source file containing data about consumed power, convert the units and time interval and write the converted data to another file.')
    parser.add_argument('input_filename', help ='The name of the file containing the data that needs to be converted.') # user specifies: value # https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument('output_filename', help = 'The name of the converted output file.')
    parser.add_argument('--interval', type=int, default=15, choices=[1, 15, 30, 60, 1440], help = 'This parameter specifies the target interval in minutes.')  # user specifies: --name value # https://docs.python.org/3/library/argparse.html#choices
    parser.add_argument('--unit', default="Wh", choices=["kWh", "Wh", "KJ", "J"], help = 'This parameter specifies the target power unit. Unit input is case sensitive.')
    args = parser.parse_args()
    return args
def converter(args: Namespace, conv_dict: dict):
    target_interval: int = args.interval
    target_unit: str = args.unit

    with open(args.input_filename, "r") as my_file, open(args.output_filename, "w") as output:
        data = my_file.read()
        data = json.loads(data)
        data_output = copy.copy(data)
        data_array = data["data"]

        source_interval = data["interval_in_minutes"]
        data_output["interval_in_minutes"] = target_interval
        converted_data = change_interval(data_array, source_interval, target_interval)
        data_output["data"] = converted_data

        # data to unit:
        file_unit = data["unit"]
        data_output["unit"] = target_unit
        if file_unit != target_unit:
            converted_data_units = change_units(conv_dict, converted_data, file_unit, target_unit)
            data_output["data"] = converted_data_units
        # writing the file:
        result = json.dump(data_output, output)
        return result
def change_units(conv_dict, data_array, file_unit, target_unit):
    converted_data_units = []
    for e in data_array:
        e *= conv_dict[target_unit] / conv_dict[file_unit]
        converted_data_units.append(e)
    return converted_data_units
def change_interval(data_array, source_interval, target_interval):
    # interval more frequent to less frequent data:
    converted_data = []

    if source_interval < target_interval:
        interval_step = target_interval // source_interval
        for i in range(0, len(data_array), interval_step):
            val_new = (sum(data_array[i: i + interval_step])) / interval_step
            converted_data.append(val_new)
    # interval less frequent to more frequent data:
    elif source_interval > target_interval:
        interval_step = source_interval // target_interval
        for e in data_array:
            for i in range(0, interval_step):
                converted_data.append(e)
    else:
        converted_data = data_array
    return converted_data

if __name__ == "__main__":
    conv_units = {}
    conv_units["kWh"] = float(0.001)  # unit * target / file unit
    conv_units["Wh"] = 1
    conv_units["KJ"] = float(3.6)
    conv_units["J"] = 3600

    args = setup_argparse()
    converter(args, conv_units)