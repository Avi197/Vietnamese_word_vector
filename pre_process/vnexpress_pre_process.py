import jsonlines
import os
from Word_vector_github import file_path

Vnexpress_infile = file_path.Vnexpress
Vnexpress_data = file_path.Vnexpress_data

filename = os.path.dirname(Vnexpress_data)
if not os.path.exists(filename):
    os.makedirs(filename)


"""
Vnexpress tags are broken but we don't care about it here
some title are just broken, very short, make no sense, contain half a word, or a single character, ... titles might be 
cut off after the dash symbol, e.g: máy bay F-22 => máy bay F (possibly bad crawling)
"""


def get_data_vnexpress(infile):
    count_line = 1

    with jsonlines.open(infile) as infile:
        with jsonlines.open(Vnexpress_data, 'w') as outfile:
            for obj in infile:
                # only titles end with ' ' (space character) are broken (good stuff)
                if not obj['title'].endswith(' '):
                    outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Vnexpress_data}')


get_data_vnexpress(Vnexpress_infile)
