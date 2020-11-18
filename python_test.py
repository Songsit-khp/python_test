data = [
    {
        "key": 1,
        "value": 3,
    },
    {
        "key": 1,
        "value": 2,
    },
    {
        "key": 1,
        "value": 3,
    },
    {
        "key": 2,
        "value": 2,
    },
    {
        "key": 2,
        "value": 3,
    },
    {
        "key": 1,
        "value": 2,
    }
]

key_data = []

for dict in data:
    if dict['key'] not in key_data:
        key_data.append(int(dict['key']))

result = []
for key in key_data:
    data_list = []
    for meta in data:
        if meta['key'] == key and len(data_list) < 3:
            data_list.append(meta['value'])
    data_json = {
        "key_data": key,
        "all_value": data_list,
        "sum_value": sum(data_list)
    }
    result.append(data_json)

print(result)