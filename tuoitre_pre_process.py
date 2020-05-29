import jsonlines
from langdetect import detect
from . import file_path

Tuoitre_infile = file_path.Tuoitre
Tuoitre_data = 'H:/Vietnamese word representations/Word_vector_data/Tuoitre/tuoitre_data.json'

"""

"""


def get_tuoitre_vnexpress(infile):
    count_line = 1

    with jsonlines.open(infile) as file:
        with jsonlines.open(Tuoitre_data, 'w') as outfile:
            for obj in file:
                if obj['title'] == 'Noname':
                    obj['title'] = ''
                outfile.write(obj)
                print(f'done line {count_line}')
                count_line += 1
            print(f'wrote to {Tuoitre_data}')


get_tuoitre_vnexpress(Tuoitre_infile)
