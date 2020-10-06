import json
import copy


path = "H:/Vietnamese word representations/Word_vector_data/datafile_count.txt"
path_2 = "H:/Vietnamese word representations/Word_vector_data/datafile_count_.txt"
with open(path, 'r', encoding='utf-8') as infile:
    data = json.load(infile)
    # data_copy = copy.deepcopy(data)
    for key, value in list(data.items()):
        if int(value) <= 100:
            del data[key]
    with open(path_2, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=2)
