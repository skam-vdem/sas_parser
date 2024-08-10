import json
import os
import datetime


def extract_values(data_json):
    result = {}
    current_title = None
    current_duration = None

    if isinstance(data_json, dict):
        for key, value in data_json.items():
            if key == "title":
                current_title = value
            elif key == "duration":
                current_duration = str(value)
            if isinstance(value, (dict, list)):
                nested_result = extract_values(value)
                result.update(nested_result)

        if current_title and current_duration is not None:
            result[current_title] = current_duration

    elif isinstance(data_json, list):
        for item in data_json:
            result.update(extract_values(item))

    return result


json_files = [
    'test_1.json', 'test_2.json', 'test_3.json', 'test_4.json', 'test_5.json',
    'test_6.json', 'test_7.json', 'test_8.json', 'test_9.json', 'test_10.json'
]

combined_dict = {}


for json_file in json_files:
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            extracted_dict = extract_values(data)
            combined_dict.update(extracted_dict)
    else:
        print(f"Файл {json_file} не найден.")

average_length = datetime.timedelta(hours=0, minutes=0)
count_list = []
for value in combined_dict.values():
    second = value[len(value)-2] + value[len(value)-1]
    if len(value) == 5:
        minute = value[len(value)-5]
        + value[len(value)-4]
        + value[len(value)-3]
    else:
        minute = value[len(value)-4] + value[len(value)-3]
    hour = int(minute) // 60
    minute = int(minute) % 60
    count_list.append(datetime.timedelta(hours=hour, minutes=minute))
    print(datetime.timedelta(hours=hour, minutes=minute))
for time in count_list:
    average_length += time
average_length = average_length / 200
print(average_length)
