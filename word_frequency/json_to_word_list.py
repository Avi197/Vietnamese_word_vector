import json
import copy


path = "H:/Vietnamese word representations/Word_vector_data/datafile_count_less_than_1000.txt"
output_path = "H:/Vietnamese word representations/Word_vector_data/word_list_less_than_1000"

with open(path, 'r', encoding='utf-8') as infile:
    data = json.load(infile)
    # data_copy = copy.deepcopy(data)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for key, value in list(data.items()):
            outfile.write(key + '\n')

