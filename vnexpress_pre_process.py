import jsonlines
from langdetect import detect
from . import file_path

Vnexpress_infile = file_path.Vnexpress
Vnexpress_data = 'H:/Vietnamese word representations/Word_vector_data/Vnn/vnn_data.json'

"""
Vnexpress tags are broken but we don't care about it here
some title are just broken, very short, make no sense, contain half a word, or a single character, ... titles might be 
cut off after the dash symbol, e.g: máy bay F-22 => máy bay F (possibly bad crawling)
"""


def get_data_vnexpress(infile):
    count_line = 1

    with jsonlines.open(infile) as file:
        with jsonlines.open(Vnexpress_data, 'w') as outfile:
            for obj in file:
                # only titles end with ' ' (space character) are broken (good stuff)
                if not obj['title'].endswith(' '):
                    outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Vnexpress_data}')


get_data_vnexpress(Vnexpress_infile)
