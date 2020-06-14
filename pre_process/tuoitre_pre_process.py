import jsonlines
import os
from Word_vector_github import file_path

Tuoitre_infile = file_path.Tuoitre
Tuoitre_data = file_path.Tuoitre_data

filename = os.path.dirname(Tuoitre_data)
if not os.path.exists(filename):
    os.makedirs(filename)

"""
remove "Noname" titles
"""


def get_tuoitre_vnexpress(infile):
    count_line = 1

    with jsonlines.open(infile) as infile:
        with jsonlines.open(Tuoitre_data, 'w') as outfile:
            for obj in infile:
                if obj['title'] == 'Noname':
                    obj['title'] = ''
                outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Tuoitre_data}')


get_tuoitre_vnexpress(Tuoitre_infile)
