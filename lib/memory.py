import json

MEMORY_INF = {
    "CIN": "cin"
}

def save_to_memory(data, inf):
    with open("data/memory.json") as jsonf:
        json_data = json.load(jsonf)
        json_data[inf].append(data)

        with open("data/memory.json", "w") as outf:
            json.dump(json_data, outf)

def read_from_memory(inf):
    with open("data/memory.json") as jsonf:
        json_data = json.load(jsonf)

    return json_data[inf]
