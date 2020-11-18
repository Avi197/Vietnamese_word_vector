import json
import copy


path = "/Word_vector_data/datafile_count.txt"
output_path = "H:/Vietnamese word representations/Word_vector_data/datafile_count_less_than_"

num = 1000

with open(path, 'r', encoding='utf-8') as infile:
    data = json.load(infile)
    # data_copy = copy.deepcopy(data)
    for key, value in list(data.items()):
        if int(value) <= num:
            del data[key]
    with open(output_path + str(num) + '.txt', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
