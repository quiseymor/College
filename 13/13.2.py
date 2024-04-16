import json

def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def calculate_sum(data):
    result = 0
    for item in data:
        result += item['score'] * item['weight']
    return round(result, 3)

file_name = 'data.json'
data = read_json_file(file_name)

result = calculate_sum(data)
print(result)